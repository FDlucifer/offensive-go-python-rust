from typing import List

baseCosts = [1,7]
toppingCosts = [3,4]
target = 10

def closestCost(baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
    ans = min(baseCosts)
    def dfs(p: int, cur_cost: int) -> None:
        nonlocal ans
        if abs(ans - target) < cur_cost - target:
            return
        if abs(ans - target) >= abs(cur_cost - target):
            if abs(ans - target) > abs(cur_cost - target):
                ans = cur_cost
            else:
                ans = min(ans, cur_cost)
        if p == len(toppingCosts):
            return
        dfs(p + 1, cur_cost + toppingCosts[p] * 2)
        dfs(p + 1, cur_cost + toppingCosts[p])
        dfs(p + 1, cur_cost)
    for c in baseCosts:
        dfs(0, c)
    return ans


print(closestCost(baseCosts, toppingCosts, target))