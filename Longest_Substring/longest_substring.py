class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_sub_string = []
        for i in range(len(s)):
            current = []
            for j in range(i,len(s)):
                if s[j] not in current:
                    current.append(s[j])
                else:
                    break
            if len(current) > len(max_sub_string):
                max_sub_string = current
        return len(max_sub_string)    
    
# Time complexity is O(n^2) 