def strong_password_changes(s):
    # The function takes an input string 's' which is a password and returns the minimum number of changes needed to make it a strong password.
    # A strong password is 6-20 characters long and contains at least one lowercase letter, one uppercase letter, and one digit. It also doesn't have three repeating characters in a row.
    # Initialize variables to track the number of changes and the requirements
    
    # These variables will be initialized to 0 and they are used to track if the password has a lowercase letter, uppercase letter, and digit
    has_lowercase = 0
    has_uppercase = 0
    has_digit = 0
    
    # These variables will be initialized to 0 and they are used to track the number of changes needed for repeating characters and missing character types
    repeat_changes = 0
    character_changes = 0
    # This variable will be initialized to 0 and it is used to track the minimum number of changes needed
    min_changes = 0
    i = 2
    
    # Iterate through the characters in the string to check if the password has a lowercase letter, uppercase letter, and digit
    for c in s:
        # Check for lowercase, uppercase, and digit
        if c.islower():
            has_lowercase = 1
        elif c.isupper():
            has_uppercase = 1
        elif c.isdigit():
            has_digit = 1
    
    # Calculate the number of changes needed for repeating characters
    # Iterate through the password, checking for groups of three repeating characters
    while i < len(s) and i < 20 :
        if s[i] == s[i - 1] == s[i - 2]:
            length = 2
            # Continue checking for repeating characters in the group
            while i < len(s) and s[i] == s[i-1] and i < 20:
                length += 1
                i += 1
            # Update the number of changes needed to break up groups of three repeating characters
            repeat_changes += length // 3
        else:
            i += 1

        
    # Calculate the number of changes needed for missing character types
    character_changes = 3 - has_lowercase + has_uppercase + has_digit
    
    # Check if the length of the password is outside the 6 to 20 characters range
    if len(s) < 6:
        # If there are fewer than 6 characters, add the repeat changes and the maximum of the character changes and the number of characters that are less than needed
        min_changes=repeat_changes + max(character_changes, 6 - len(s))
    elif len(s) > 20:
        # If there are more than 20 characters, add the maximum of the repeat changes and character changes to the number of characters that are more than needed
        min_changes= max(repeat_changes, character_changes) + len(s) - 20
    else:
        # If the password length is within the acceptable range, use the maximum of the repeat changes and character changes as the minimum number of changes needed
        min_changes = max(repeat_changes, character_changes)
    return min_changes

# Test the function
password = "11aAa"
print(strong_password_changes(password))

