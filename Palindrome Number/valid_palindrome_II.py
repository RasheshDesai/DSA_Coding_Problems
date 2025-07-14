def validPalindrome(s: str) -> bool:
    def is_palindrome(s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            # Check both possibilities: skip left or skip right
            return is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1)
        left += 1
        right -= 1
    return True

print(validPalindrome(s="abca"))