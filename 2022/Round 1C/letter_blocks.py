from collections import defaultdict
from typing import List

test_case_amount = int(input())
test_cases = []


class Tower:
    def __init__(self, tower: str):
        self.as_str = tower
        self.as_list = list(tower)
        self.left = tower[0]
        self.right = tower[-1]

        self.shrinked = self.shrink(tower)

    def shrink(self, tower):
        new_tower = [tower[0]]

        for i in range(1, len(tower)):
            if tower[i] == tower[i - 1]:
                continue
            new_tower.append(tower[i])

        return new_tower

    def get_center(self):
        if len(self.shrinked) < 3:
            return []

        return self.shrinked[1:-1]


for _ in range(test_case_amount):
    _ = int(input())
    towers = [Tower(x) for x in input().split(" ")]
    test_cases.append(towers)


def is_all_unique_letters(tower):
    return len(set(tower)) == len(tower)


solutions = defaultdict(list)


def visit(
    tower: Tower,
    lefts,
    all_towers,
    target_len,
    test_case_index,
    mega_tower="",
    visited=set(),
):
    if tower.as_str in visited:
        return False

    # Get all towers in correct order
    letter_connected = lefts[tower.right]
    not_letter_connected = [tower for tower in towers if tower not in letter_connected]
    visitable = letter_connected + not_letter_connected

    visited.add(tower.as_str)
    mega_tower += tower.as_str

    if len(visited) == target_len:
        solutions[test_case_index].append(mega_tower)
        return True

    return any(
        [
            visit(
                tower,
                lefts,
                target_len,
                all_towers,
                test_case_index,
                mega_tower,
                visited,
            )
            for tower in visitable
        ]
    )


def get_answer(towers: List[Tower]):
    impossible = "IMPOSSIBLE"
    all_center_letters = []

    for tower in towers:
        if not is_all_unique_letters(tower.shrinked):
            return impossible

        # Add all center letters
        all_center_letters.extend(tower.get_center())

    if not is_all_unique_letters(all_center_letters):
        return impossible

    lefts = defaultdict(list)
    rights = defaultdict(list)

    # Get edges of towers
    for tower in towers:
        lefts[tower.left].append(tower)
        rights[tower.right].append(tower)

    # Find entrypoints
    entrypoints = set(lefts.keys())
    for key in rights.keys():
        try:
            entrypoints.remove(key)
        except:
            pass

    # Check all possible variants
    for entrypoint in entrypoints:
        any(
            [visit(tower, lefts, towers, len(towers), i) for tower in lefts[entrypoint]]
        )

    if not solutions.get(i):
        return impossible

    return solutions[i][0]


for i, towers in enumerate(test_cases):
    answer = get_answer(towers)

    print(f"Case #{i + 1}: {answer}")
