from inspect import currentframe

def get_line_number():
    # cf = currentframe()
    # return cf.f_back.f_lineno
    return currentframe().f_back.f_lineno





print ("This is line 7, python says line ", get_line_number())