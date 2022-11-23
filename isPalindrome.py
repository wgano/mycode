class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = list(str(x))
        m = n[::-1]
        return m == n
