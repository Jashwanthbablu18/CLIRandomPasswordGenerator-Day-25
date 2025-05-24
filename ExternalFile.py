# ExternalFile.py

# This imports random and string modules
import random
import string

# This function is used to generate password based on length and useSpecialChars params, it keeps use_special_chars as True by default.
def generate_password(length=12, use_special_chars = True):

    # ## If you want to see what characters are used to generate the secure/strong password, uncomment below 3 print statements.
    # print(string.ascii_letters) ## Displays all characters like UPPERCASE letters and LOWERCASE letters which are available on keyboard.
    # print(string.digits) ## Displays all NUMBERS from 0-9 which are available on keyboard.
    # print(string.punctuation) ## Displays all SPECIAL CHARACTERS available on keyboard.

    # This validates that password must be atleast 6 chars
    if length < 6:
        return "❌ Password length should be at least 6 characters."
    
    # This combines all alphabets and numbers as a string.
    chars = string.ascii_letters + string.digits
    # If user choose use_special_chars is True then it adds special characters to that string, if false(no need) then won't add.
    if use_special_chars:
        chars += string.punctuation

    # this one generates the password by randomly selects characters from(chars variable) and includes length of password, and returns it.
    password = ''.join(random.sample(chars, length))
    return password
