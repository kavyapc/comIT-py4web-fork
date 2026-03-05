# --------------------------------------------------------------
# Challenge 2 — Username Validator
# Write a function called is_valid_username(username) that
# returns True only if ALL of these conditions are met:
#   - Length is between 4 and 16 characters (inclusive)
#   - Contains only alphanumeric characters
#   - Starts with a letter (not a digit)
#   - Is all lowercase
# Test it with at least four different usernames.
# Methods: isalnum(), isalpha(), islower(), len()
# --------------------------------------------------------------

def divisor():
    """
    No argument function with no return value that
    prints a screen sepatator:
    ______________________________

    ******************************
    ______________________________

    """
    print("_" * 30 + "\n")
    print("*" * 30) 
    print("_" * 30 + "\n")
    
# divisor()

def tests(function):
    print(f"\nFunction: {function.__name__}")
    print("True - ", function("alice"))      
    print("False — uppercase  -", function("Alice"))  
    print("False — starts with digit -", function("4alice"))      
    print("False — too short -", function("ab"))        
    print("False — too long -", function("abdsgfdsfgsdfgsdfgdsfgdsfgsdfgsdfgsdfer"))    

    
    

def is_valid_username(username):
    if len(username) >= 4:
        if len(username) <= 16:
            if username.isalnum():
                if username[0].isalpha():
                    if username.islower():
                        return True
    return False

divisor()
tests(is_valid_username)


def is_valid_username_2(username):
    return (len(username )>= 4
            and len(username) <= 16 
            and username.isalnum() 
            and username[0].isalpha() 
            and username.islower())
    
divisor()
tests(is_valid_username_2)



def is_valid_username_3(username):
    if len(username) < 4:
        return False
    if len(username) > 16:
        return False
    if not username.isalnum():
        return False
    if not username[0].isalpha():
        return False
    if not username.islower():
        return False
    
    return True    

divisor()
tests(is_valid_username_3)
