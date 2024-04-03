from lib.password_checker import *
import pytest 


def test_valid_password():
    checker = PasswordChecker()
    assert checker.check("validpassword") == True

def test_invalid_password():
    checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        checker.check("short")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."








#     self.assertTrue(checker.check("valid password"))

# def test_incorrect_password(self):
#     checker = PasswordChecker()
#     with self.assertRaises(Exception) as context:
#         checker.check("short")
#     self.assertEqual(str(context.exception)), 



