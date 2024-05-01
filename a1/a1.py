"""Module for Currency Exchange"""
import introcs

def before_space(s):
    idx = s.find(" ")
    return s[:idx] 

def after_space(s):
    index = s.find(" ")
    return s[index:]

def first_inside_quotes(s):
    p1= s.find("\"")
    sUpdated = s[p1+1:]
    p2 =sUpdated.find("\"")
    return sUpdated[0:p2]

def get_lhs(json):
    return eval(json)["lhs"]
def get_rhs(json):
    return eval(json)["rhs"]
def has_error(json):
    return eval(json)["err"] != "" 
def query_website(old,new,amt):
    return introcs.urlread(f'http://cs1110.cs.cornell.edu/2022fa/a1?old={old}&new={new}&amt={amt}')
def is_currency(code):
    return has_error(query_website(code,"USD",1))

def exchange(old,new,amt):
    try:
        json = query_website(old,new,amt)
        factor = float(before_space(get_rhs(json))) / float(before_space(get_lhs(json))) 
        return amt * factor
    except:
        print("Invalid Currency Code")