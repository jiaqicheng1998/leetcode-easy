# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word 
# or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

def isAnagram(s,t):
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        for j in t:
            if j in d:
                d[j] -= 1
            else:
                return False

        for m in d.values():
            if m != 0:
                return False
        return True 

print(isAnagram("anagram","nagaram"))
print(isAnagram('rat', 'car'))
print(isAnagram('aacc', 'ccac'))
print(isAnagram("ab", "a"))
print(isAnagram("a", "aa"))
