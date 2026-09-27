class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = True
        cleaned_str = ""
        for char in s:
            if char.isalnum():
                cleaned_str += char
        cleaned_str = cleaned_str.lower()
        length = len(cleaned_str)
        for i in range(length):
            if i == length//2:
                break
            if cleaned_str[i] != cleaned_str[length-1-i]:
                result = False
                break
        return result