import os
import re


with open(os.path.join(os.path.dirname(__file__), f"input.txt")) as f:
    actual_input = f.read()

data, medicine = actual_input.split("\n\n")
replacements = dict(
    (replacement.split(" => ")[::-1] for replacement in data.splitlines())
)


possible_molecules = set()
for replacement, initial in replacements.items():
    for m in re.finditer(initial, medicine):
        possible_molecules.add(
            medicine[: m.span()[0]] + replacement + medicine[m.span()[1] :]
        )
print(f"Part 1: {len(possible_molecules)}")


class DeadEnd(Exception):
    """Used to indicate dead end"""


# A* search to find the recipe length
def recipe_length(seed, length=0):
    if seed == "e":
        return length

    # Grab the possible next steps
    next_steps = set()
    for initial, replacement in replacements.items():
        for m in re.finditer(initial, seed):
            next_steps.add(seed[: m.span()[0]] + replacement + seed[m.span()[1] :])

    # A* bit... sort the options by estimated cost (use length as proxy)
    next_steps = sorted(sorted(next_steps, reverse=True), key=len)

    # Try the next steps until we find one that isn't a dead end
    while next_steps:
        try:
            return recipe_length(next_steps.pop(0), length + 1)
        except DeadEnd:
            ...
    raise DeadEnd


print(f"Part 2: {recipe_length(medicine)}\n")