poured = 2
query_glass = 1
query_row = 1

def champagneTower(poured: int, query_row: int, query_glass: int) -> float:
    row = [poured]
    for i in range(1, query_row + 1):
        nextRow = [0] * (i + 1)
        for j, volume in enumerate(row):
            if volume > 1:
                nextRow[j] += (volume - 1) / 2
                nextRow[j + 1] += (volume - 1) / 2
        row = nextRow
    return min(1, row[query_glass])


print(champagneTower(poured, query_glass, query_row))