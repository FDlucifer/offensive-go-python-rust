class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left_distance = 0
        right_distance = 0
        underline = 0

        for move in moves:
            if move == 'L':
                left_distance += 1
            elif move == 'R':
                right_distance += 1
            elif move == '_':
                underline += 1
        if left_distance >= right_distance:
            return left_distance + underline - right_distance
        elif left_distance <= right_distance:
            return right_distance + underline - left_distance


s = Solution()
moves = "L_RL__R"
print(s.furthestDistanceFromOrigin(moves))
