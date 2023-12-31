"""
12. Integer to Roman

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.

"""





def intToRoman(num: int) -> str:
    roman = ''
    roman_dict = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
    for i in roman_dict.keys() :
        roman += roman_dict[i]*(num//i)     # add roman symbol to the result
        num = num%i                         # update no. to remaining value
        if num == 0 :
            break
    return roman


print(intToRoman(3))      # Output ==> III
print(intToRoman(333))              #  CCCXXXIII
print(intToRoman(58))               #  LVIII
print(intToRoman(1994))             #  MCMXCIV
