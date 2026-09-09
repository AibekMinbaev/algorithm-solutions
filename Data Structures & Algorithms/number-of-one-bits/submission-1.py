class Solution:
    def hammingWeight(self, n: int) -> int:
        res = sum([(i and 1) for i in bin(n) if i == "1"])
        return res 