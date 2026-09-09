class Solution:
    def hammingWeight(self, n: int) -> int:
        res = sum([1 for i in bin(n) if i == "1"])
        return res 