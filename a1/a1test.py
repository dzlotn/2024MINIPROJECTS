"""Test Script for A1"""
import introcs
import a1.a1 as a1
import json

def testA():
    string = "Hello world"
    sting2 = 'A "B C" D'
    introcs.assert_equals("Hello", a1.before_space(string),"Test A.1 Passes")
    introcs.assert_equals(" world",a1.after_space(string), "Test A.2 Passes")
    print(a1.first_inside_quotes(sting2))
    dictionary = eval(introcs.urlread('http://cs1110.cs.cornell.edu/2022fa/a1?old=USD&new=CUP&amt=2.5'))
    # dictionary["lhs"].split(" ")
    print(eval(json)["err"] )
    print(a1.has_error(json))
    pass
testA()
