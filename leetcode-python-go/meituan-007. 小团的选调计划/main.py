n = int(input())
chosen = []
for i in range(n):
    l = list(input().split())
    for num in l:
        if num not in chosen:
            chosen.append(num)
            break
print(' '.join(chosen))