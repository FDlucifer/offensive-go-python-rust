from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        buy_price = prices[0]  # 初始化购买价格为第一天的股价
        max_profit = 0  # 初始化最大利润为0

        for price in prices:
            if price < buy_price:
                buy_price = price  # 如果当前股价更低，更新购买价格
            else:
                max_profit = max(max_profit, price - buy_price)  # 计算当前利润并更新最大利润

        return max_profit



s = Solution()
prices = [7,1,5,3,6,4]
print(s.maxProfit(prices))
