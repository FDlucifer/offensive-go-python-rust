mask=1065233
s = "textbook"

def countVowel(t:str)->int:
    return sum(mask&(1<<(ord(c)-97))>0 for c in t)

def halvesAreAlike(s: str) -> bool:
	s=s.lower()
    return countVowel(s[:len(s)>>1])==countVowel(s[len(s)>>1:])

print(halvesAreAlike(s))