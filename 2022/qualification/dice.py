test_case_amount = int(input())
test_cases = []

for _ in range(test_case_amount):
    dice_amount = int(input())
    dices = [int(x) for x in input().split()]
    test_cases.append([dice_amount, dices])

for test_case_number, (dice_amount, dices) in enumerate(test_cases):
    print(f"Case #{test_case_number + 1}: ", end="")

    dices.sort()

    dice_index = 0
    number = 0

    while dice_index < dice_amount:
        if dices[dice_index] < number + 1:
            dice_index += 1
        else:
            dice_index += 1
            number += 1
    print(number)
