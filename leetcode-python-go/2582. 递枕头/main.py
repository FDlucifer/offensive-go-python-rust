class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direction = 1  # Initial direction
        i = 1  # Initial index

        while time > 0:
            # Update the current index with the current direction
            i += direction

            # If the index reaches the end of the line, change direction
            if i == n + 1:
                direction = -1
                i = n - 1
            elif i == 0:
                direction = 1
                i = 2

            # Reduce the remaining time by 1 second
            time -= 1

        return i


s = Solution()
n = 4
time = 5
print(s.passThePillow(n, time))
