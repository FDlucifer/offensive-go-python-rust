class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        nums = [1] * numOnes + [0] * numZeros + [-1] * numNegOnes
        return sum(nums[:k])



s = Solution()
numOnes = 3
numZeros = 2
numNegOnes = 0
k = 2
print(s.kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k))
