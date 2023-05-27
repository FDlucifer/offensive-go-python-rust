class Solution:
    def buyChoco(self, prices, money):
        prices.sort()  # 对价格数组进行排序
        lowchoice = prices[0] + prices[1]
        if lowchoice > money:
            return money
        elif lowchoice <= money:
            return money - lowchoice


s = Solution()
prices = [98,54,6,34,66,63,52,39]
money = 62
print(s.buyChoco(prices, money))
