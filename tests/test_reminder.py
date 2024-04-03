# import pytest
from lib.reminder import *

def test_reminds_the_user_to_do_a_task():
    reminder = Reminder("Kay")
    reminder.remind_me_to("Walk the dog")
    result = reminder.remind()
    assert result == "Walk the dog, Kay!"
    
# For the test to fail
# def test_reminder():
#     reminder = Reminder("kay")
#     with pytest.raises(Exception) as e: # new code
#         reminder.remind()
#     error_message = str(e.value) # new code
#     assert error_message == "No reminder set!"



