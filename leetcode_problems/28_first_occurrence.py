'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.

'''



def strStr(haystack: str, needle: str) -> int:
    index = haystack.find(needle)   # returns -1 if substring not found in string
    return index

print(strStr("sadbutsad", "sad"))     # =>  0
print(strStr("leetcode", "leeto"))    # => -1