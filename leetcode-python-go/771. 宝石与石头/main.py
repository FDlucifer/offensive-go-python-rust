class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(1 for stone in stones if stone in jewels)

s = Solution()
jewels = "aA"
stones = "aAAbbbb"
print(s.numJewelsInStones(jewels, stones))
