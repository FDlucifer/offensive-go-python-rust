from collections import defaultdict
import re


def parse(stream):
    replacements = defaultdict(list)
    for k, v in re.findall(r"(\w+) => (\w+)", stream):
        replacements[k].append(v)
    return replacements, stream.strip().split("\n")[-1]


def reverse_dict(d):
    reverse = defaultdict(list)
    for k, v in d.items():
        for i in v:
            reverse[i].append(k)
    return reverse


def generate_next(starter, replacements):
    molecules = set()

    for i, char in enumerate(starter):
        try:
            if char in replacements:
                for replacement in replacements[char]:
                    molecules.add(starter[:i] + replacement + starter[i + 1:])
            else:
                for replacement in replacements[starter[i:i + 2]]:
                    molecules.add(starter[:i] + replacement + starter[i + 2:])
        except KeyError:
            continue

    return molecules


def generate_prev(target, replacements):
    molecules = set()

    for k, v in replacements.items():
        idx = target.find(k)
        while idx >= 0:
            for i in v:
                if i == "e":
                    continue
                try:
                    molecules.add(target[:idx] + i + target[idx + len(k):])
                except IndexError:
                    molecules.add(target[:idx] + i)
            idx = target.find(k, idx+1)

    if not molecules:
        molecules = {"e"}
    return molecules


def count_molecules(starter, replacements):
    return len(generate_next(starter, replacements))


def steps_to_generate(target, replacements):
    replacements = reverse_dict(replacements)
    seen = {}
    last_generation = generate_prev(target, replacements)
    n_steps = 1

    while last_generation != {"e"}:
        current_generation = set()
        molecule = min(last_generation, key=len)

        try:
            new_molecules = seen[molecule]
        except KeyError:
            new_molecules = generate_prev(molecule, replacements)
            seen[molecule] = new_molecules
        current_generation |= new_molecules
        last_generation = current_generation

        n_steps += 1

    return n_steps


def part_one():
    with open("input.txt") as fin:
        replacements, starter = parse(fin.read())
    print(count_molecules(starter, replacements))


def part_two():
    with open("input.txt") as fin:
        replacements, target = parse(fin.read())
    print(steps_to_generate(target, replacements))


if __name__ == '__main__':
    part_one()
    part_two()