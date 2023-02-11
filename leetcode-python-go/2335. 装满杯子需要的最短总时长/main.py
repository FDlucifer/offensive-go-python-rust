from typing import List

amount = [5,4,4]

def fillCups(amount: List[int]) -> int:
    amount.sort()
    if amount[2] > amount[1] + amount[0]:
        return amount[2]
    return (sum(amount) + 1) // 2

print(fillCups(amount))