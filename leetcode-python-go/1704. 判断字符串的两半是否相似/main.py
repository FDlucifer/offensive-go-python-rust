s = "textbook"

def halvesAreAlike(s: str) -> bool:
	VOWELS = "aeiouAEIOU"
	a, b = s[:len(s) // 2], s[len(s) // 2:]
	return sum(c in VOWELS for c in a) == sum(c in VOWELS for c in b)

print(halvesAreAlike(s))