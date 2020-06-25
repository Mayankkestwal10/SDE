class Solution:
    def trailingZeroes(self, n: int) -> int:
        total = 0
        while(n>=5):
            temp = n//5
            n = temp
            total+=temp
        return total