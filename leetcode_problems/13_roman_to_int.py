'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000


'''




def romanToInt(s: str) -> int:
	roman = {'I':1, 'V':5, "X":10, "L":50, "C":100, "D":500, "M":1000}
	result = 0

	# iterate through each character in the roman numeral string
	for i in range(len(s)) :
		# check if the value of current character is less than the value of next character
		if i+1 < len(s) and roman[s[i]] < roman[s[i+1]] :       
			result -= roman[s[i]]
		else :
			result += roman[s[i]]
	return result

print(romanToInt("III"))       # => 3
print(romanToInt("LVIII"))     # => 58
print(romanToInt("MCMXCIV"))   # => 1994