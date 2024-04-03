from lib.report_length import *

def test_report_length_of_a_given_string():
    assert report_length("") == "This string was 0 characters long."
    assert report_length("Hello") == "This string was 5 characters long."
    assert report_length("1234567") == "This string was 7 characters long."
    assert report_length("My name is Jennifer") == "This string was 19 characters long."