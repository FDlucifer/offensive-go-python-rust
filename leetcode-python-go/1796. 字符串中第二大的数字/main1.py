import re

s = "dfa12321afd"

def secondHighest(s: str) -> int:
    return sorted([-1, -1] + [int(i) for i in set(''.join(re.findall('\d+', s)))])[-2]

print(secondHighest(s))