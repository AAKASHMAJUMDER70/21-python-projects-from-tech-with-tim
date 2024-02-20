def password_generator(length_of_the_password_to_be_generated):

    import re
    import string
    import random

    uppercase_char = string.ascii_uppercase
    lowercase_char = string.ascii_lowercase
    digits = string.digits
    special_char = r"`~!@#$%^&*()-=_+;':\"[]{}|,./<>?"

    pattern = uppercase_char+lowercase_char+digits+special_char

    pattern = re.escape(pattern)
    
    password_generated = "".join(random.sample(pattern,length_of_the_password_to_be_generated))
    
    print (password_generated)

password_generator(22)

