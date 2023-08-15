'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

'''


def lengthOfLastWord(s):
    trimmed_s = s.strip()           # removing spaces at the begining & at the end
    words = trimmed_s.split()       # split words using spaces
    last_word = words[-1]           # find last word from the list of words
    return len(last_word)           # return the length of last word


print(lengthOfLastWord("Hello World"))                  # => 5
print(lengthOfLastWord("   fly me   to   the moon  "))  # => 4
print(lengthOfLastWord("luffy is still joyboy"))        # => 6