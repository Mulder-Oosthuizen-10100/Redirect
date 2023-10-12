import gspread
import re
from datetime import datetime

sa = gspread.service_account()
sh = sa.open('WEBSITE_DATA')
wks_websites = sh.worksheet('WEBSITES')
wks_keywords = sh.worksheet('KEYWORDS')
wks_remove_part = sh.worksheet('REMOVE_PARTS')

directory = input("Enter the folder location: ")

all_web_sites = wks_websites.get_all_records()

print("")
print("List of Websites:")
print("=================")

for wb in all_web_sites:
    print(" - " + wb.get('WEBSITE'))

print("")

input_website = input("Enter a Website Name from the above list: ")

for wb in all_web_sites:
    if wb.get('WEBSITE').upper() == input_website.upper():
        working_website = input_website.upper()
        break    

all_remove_parts = wks_remove_part.get_all_records()

for rp in all_remove_parts:
    web = rp.get('WEBSITE').upper()
    if web == working_website:
        remove_part = rp.get('REMOVE_PART').lower()
        if remove_part == '':
            do_remove_part = False
        else:
            do_remove_part = True
        break

# remove_part = input('Enter the REMOVE PART of the URL: ')
f = open(directory, "r")
datetimestr = datetime.now()
dt_string = datetimestr.strftime("%Y_%m_%d__%H_%M_%S")
csvDirectory = re.sub('.txt', "_" + dt_string + '.csv', directory)
notFoundDirectory = "Unmatched_URLS_" + dt_string + ".txt"
nf = open(csvDirectory, 'a')
notFoundFile = open(notFoundDirectory, 'a')
all_key_words = wks_keywords.get_all_records()

for l in f:
    if l.find("?") == -1:
        new_l = re.sub("\n", "", l)
        if do_remove_part:
            new_l = re.sub(remove_part, "", new_l)
            lower_l = new_l.lower()
        for kw in all_key_words:
            if kw.get('WEBSITE').upper() == working_website:
                found_keyword = False
                if lower_l.find(kw.get('KEYWORD').lower()) != -1:
                    destinationURL = kw.get('URL')
                    nf.write(lower_l + '*,' + destinationURL + "\n")
                    found_keyword = True
                    break
                
        if not found_keyword:
            notFoundFile.write(lower_l + "\n")
            for kw in all_key_words:
                if kw.get('WEBSITE').upper() == working_website:
                    if kw.get('DEFAULT') == 'TRUE':
                        destinationURL = kw.get('URL')
                        nf.write(lower_l + '*,' + destinationURL + "\n")
                        break