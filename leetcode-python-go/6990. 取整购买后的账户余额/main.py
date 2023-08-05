class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        def traditional_round(x):
            import math
            return int(x + math.copysign(0.5, x))
        roundedAmount = traditional_round(purchaseAmount / 10) * 10
        balance = 100 - roundedAmount
        return balance

s = Solution()
purchaseAmount = 15
print(s.accountBalanceAfterPurchase(purchaseAmount))
