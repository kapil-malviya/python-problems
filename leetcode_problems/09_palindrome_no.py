"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""



def isPalindrome(x):
    if x < 0:
        return False
    
    reversed_x = 0
    original_x = x
    
    while x > 0:
        digit = x % 10                        # get last digit of x
        reversed_x = reversed_x * 10 + digit      # add digit to the reversed x
        x = x // 10                      # remove the last digit from x
    
    return original_x == reversed_x


print(isPalindrome(18881))   # return : True
print(isPalindrome(181))   # True
print(isPalindrome(-181))  # False
print(isPalindrome(10))    # False