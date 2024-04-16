# Import the needed libraries
import gspread # Integrate to google sheets
import re # String manipulation
from datetime import datetime # File date time

# sa = service account - this account is used to access the google sheets document
sa = gspread.service_account()

# sh = sheet - this will be the object that contains the sheet document
sh = sa.open('WEBSITE_DATA')

# wks_ = worksheet - this references the specific sheet inside the google sheets document
wks_websites = sh.worksheet('WEBSITES')
wks_keywords = sh.worksheet('KEYWORDS')
wks_remove_part = sh.worksheet('REMOVE_PARTS')

# The directory where the source url's (the url's that has to be redirected) are kept e.g. c:\temp\source_urls.txt
directory = input("Enter the folder location: ")

# Fetch all the records - this will give the data as a dictionary
# {
#   {"WEBSITE": "Sandman"},
#   {"WEBSITE": "TheGuy"}
# }
all_web_sites = wks_websites.get_all_records()

# Show the user the available website names that was retrieved from the sheet
print("")
print("List of Websites:")
print("=================")

# Loop through the dictionary and print each website
for wb in all_web_sites:
    print(" - " + wb.get('WEBSITE'))

print("")

# get the website name for which the redirects should be done
input_website = input("Enter a Website Name from the above list: ")

# Now we loop through the website list once more to ensure the user input matches the list of websites
for wb in all_web_sites:
    # Note: Upper both the google sheets website value and the user input value
    if wb.get('WEBSITE').upper() == input_website.upper():
        working_website = input_website.upper()
        break    

# Fetch all the records - this will give the data as a dictionary
all_remove_parts = wks_remove_part.get_all_records()

# Loop through each returned value
for rp in all_remove_parts:
    # find the working website 
    web = rp.get('WEBSITE').upper()
    if web == working_website:
        # find the part that has to be removed from the source url's
        remove_part = rp.get('REMOVE_PART').lower()
        # if the remove part for a website is empty or not found we set a flag 
        if remove_part == '':
            # do not remove anything
            do_remove_part = False
        else:
            # remove the given data
            do_remove_part = True
        break

# f = File - This file contains the source url's
f = open(directory, "r")

# set the date and time for the csv and unmatched url files
date_time_str = datetime.now()

# Format the date time to 2023_10_12__19_36_47
dt_string = date_time_str.strftime("%Y_%m_%d__%H_%M_%S")

# Take the source data file name and change it with the date time string + .csv 
csvDirectory = re.sub('.txt', "_" + dt_string + '.csv', directory)

# Take the sauce data file name and change it with the data time string
notFoundDirectory = re.sub('.txt', "_Unmatched_URLS_" + dt_string + ".txt", directory)

# nf = new file - this will contain ALL the redirected url's
nf = open(csvDirectory, 'a', encoding="utf8")

# this file will contain all the url's that received the default url
notFoundFile = open(notFoundDirectory, 'a')

# Fetch all the records - this will give the data as a dictionary
all_key_words = wks_keywords.get_all_records()

# Loop through each line of the source file
for l in f:
    # Check the read line if it contains "?" we skip it 
    if l.find("?") == -1:
        # The read line has a \n = new line or ENTER at the end and we are removing that character
        new_l = re.sub("\n", "", l)
        # If the remove part flag (line 60) is true we need to remove the part that has to be removed from the source url
        if do_remove_part:
            # Sub = substitute the remove part with an empty string
            new_l = re.sub(remove_part, "", new_l)
            # ensure the new url is a lower case url
            lower_l = new_l.lower()
        # now the url is ready for matching it with a key word. 
        # Loop through each keyword
        for kw in all_key_words:
            # find the working website
            if kw.get('WEBSITE').upper() == working_website:
                # we have to set this flag false so that when we reset the flag
                found_keyword = False
                # now we check the source url if the keyword is found
                if lower_l.find(kw.get('KEYWORD').lower()) != -1:
                    # get the redirect url 
                    destinationURL = kw.get('URL')
                    # format the csv file line 
                    nf.write(lower_l + '*,' + destinationURL + "\n")
                    # indicate that we have matched at least one keyword
                    found_keyword = True
                    # stop looping through the keywords and go to the next source file line
                    break

        # Set the default destination url
        if not found_keyword:
            # We have to add a new line character so that the file does not print one long line
            notFoundFile.write(lower_l + "\n")
            # Loop through the keywords to find the default key word
            for kw in all_key_words:
                # Check the website name is the working website name
                if kw.get('WEBSITE').upper() == working_website:
                    # Check if there is a default key word
                    if kw.get('DEFAULT') == 'TRUE':
                        # Assign the destination url
                        destinationURL = kw.get('URL')
                        # Write the destination url with the format old url + * + , + destination url + new line character so that the file does not print one long line
                        nf.write(lower_l + '*,' + destinationURL + "\n")
                        # if the default key word is found stop looping though the key words
                        break