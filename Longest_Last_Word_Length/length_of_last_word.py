# Solution One 

def lengthOfLastWord(s):
    s = s.split()
    return len(s[-1])

# Solution two

def lengthOfLastWord(s):
    s = s.split()
    length = 0
    for i in [len(s)-1]:
        length = len(s[i])
    return length

