croakOfFrogs = "crcoakroak"

def minNumberOfFrogs(croakOfFrogs: str) -> int:
    counter = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
    max_frogs = 0
    cur_frogs = 0
    for c in croakOfFrogs:
        if c not in counter:
            return -1
        counter[c] += 1
        if c == 'c':
            cur_frogs += 1
            max_frogs = max(max_frogs, cur_frogs)
        elif c == 'k':
            cur_frogs -= 1
        elif counter['c'] < counter['r'] or counter['r'] < counter['o'] or counter['o'] < counter['a'] or counter['a'] < counter['k']:
            return -1
    return max_frogs if cur_frogs == 0 else -1

print(minNumberOfFrogs(croakOfFrogs))
