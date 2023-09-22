class Solution:
    def distMoney(self, money: int, children: int) -> int:

        if money < children: return -1          #   <-- 孩子比钱多

        n = 8 * children - money                #   <-- 足够的钱给所有的孩子
                                                #       至少得到8美元;一个
        if n <= 0: return children - (n < 0)    #       孩子可能会得到超过8美元

        ans, rem = divmod(money-children,7)     #   <-- 每个孩子都得到一美元，然后答案
                                                #       儿童可额外获得7美元

        return ans - ((ans, rem) == (children - 1, 3))
                                                #   <-- 如果只有一个孩子，则减少ans
                                                #       少于8美元
                                                #       孩子正好得到4美元


s = Solution()
money = 20
children = 3
print(s.distMoney(money, children))
