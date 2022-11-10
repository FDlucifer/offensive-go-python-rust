s = "textbook"

def halvesAreAlike(s: str) -> bool:
	n = len(s)
    ans = 0
    for i, c in enumerate(s):
        if c in 'aeiouAEIOU':
            if i < n//2:
                ans += 1
            else:
                ans -= 1
    if ans == 0:
        return True

print(halvesAreAlike(s))