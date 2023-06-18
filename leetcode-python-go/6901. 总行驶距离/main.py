class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        distance = 0
        count = 0
        if mainTank // 5 >= 1:
            while mainTank > 0:
                mainTank -= 5
                count += 1
                if count <= additionalTank:
                    mainTank += 1
                distance += 50
                if mainTank < 5:
                    distance += mainTank * 10
                    break
        else:
            distance = mainTank * 10

        return distance


s = Solution()
mainTank = 8
additionalTank = 2
print(s.distanceTraveled(mainTank, additionalTank))
