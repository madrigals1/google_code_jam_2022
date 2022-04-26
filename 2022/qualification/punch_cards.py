test_case_amount = int(input())
test_cases = []


for _ in range(test_case_amount):
    line = input()
    row_amount_str, col_amount_str = line.split(" ")
    test_cases.append([int(row_amount_str), int(col_amount_str)])

for i, (row_amount, col_amount) in enumerate(test_cases):
    print(f"Case #{i + 1}:")

    dot_lines = []
    cross_lines = []

    for row in range(row_amount):
        dot_line = ""
        cross_line = ""

        for col in range(col_amount):

            if row == 0 and col == 0:
                cross_line += ".."
                dot_line += ".."
            else:
                cross_line += "+-"
                dot_line += "|."

        dot_lines.append(f"{dot_line}|")
        cross_lines.append(f"{cross_line}+")

    card = ""

    for i in range(len(cross_lines)):
        card += f"{cross_lines[i]}\n"
        card += f"{dot_lines[i]}\n"

    # Add extra line
    card += f"{cross_lines[-1]}\n"

    print(card, end="")
