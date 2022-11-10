s = "textbook"
w='aeiouAEIOU'
def halvesAreAlike(s: str) -> bool:
	return sum(c in w for c in s[:len(s)>>1])==sum(c in w for c in s[len(s)>>1:])

print(halvesAreAlike(s))