from dataclasses import dataclass


@dataclass
class Color:
    cyan: int
    magenta: int
    yellow: int
    key: int

    @property
    def sum(self):
        return self.cyan + self.magenta + self.yellow + self.key

    def __str__(self):
        return f"{self.cyan} {self.magenta} {self.yellow} {self.key}"


expected_sum = 10**6


def min_color_from_printers(printers):
    min_color = Color(cyan=10e6, magenta=10e6, yellow=10e6, key=10e6)

    for printer in printers:
        min_color.cyan = min(min_color.cyan, printer.cyan)
        min_color.magenta = min(min_color.magenta, printer.magenta)
        min_color.yellow = min(min_color.yellow, printer.yellow)
        min_color.key = min(min_color.key, printer.key)

    return min_color


test_case_count = int(input())
test_cases = []

for _ in range(test_case_count):
    test_case = []

    for _ in range(3):
        test_case.append([int(num) for num in input().split(" ")])

    test_cases.append(test_case)

for i, test_case in enumerate(test_cases):
    print(f"Case #{i + 1}: ", end="")

    printers = []

    for cyan, magenta, yellow, key in test_case:
        printers.append(Color(cyan=cyan, yellow=yellow, magenta=magenta, key=key))

    min_color = min_color_from_printers(printers)

    if min_color.sum < expected_sum:
        print("IMPOSSIBLE")
        continue

    if min_color.sum > expected_sum:
        missing = min_color.sum - expected_sum

        for part in ["cyan", "magenta", "yellow", "key"]:
            color_part = getattr(min_color, part)

            setattr(min_color, part, color_part - min(missing, color_part))

            if min_color.sum == expected_sum:
                break

            missing -= color_part

    print(min_color)
