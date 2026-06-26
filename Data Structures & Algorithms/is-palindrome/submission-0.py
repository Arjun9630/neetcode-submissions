class Solution:
    def isPalindrome(self, s: str) -> bool:
        inpt = []
        for char in s:
            if char.isalnum():
                inpt.append(char.lower())
        inpt = "".join(inpt)
        rev = inpt[::-1]
        return rev == inpt