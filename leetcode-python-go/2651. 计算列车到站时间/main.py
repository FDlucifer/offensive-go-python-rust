class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24


s = Solution()
arrivalTime = 15
delayedTime = 5
print(s.findDelayedArrivalTime(arrivalTime, delayedTime))
