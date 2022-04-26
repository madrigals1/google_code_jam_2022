from collections import deque

test_case_amount = int(input())
test_cases = []

for _ in range(test_case_amount):
    pancake_amount = int(input())
    pancakes = [int(x) for x in input().split(" ")]
    test_cases.append([pancake_amount, pancakes])

for i, (_, pancakes) in enumerate(test_cases):
    queue = deque(pancakes)

    max_so_far = 0
    paid = 0

    while queue:
        left, right = queue[0], queue[-1]

        if left < right:
            if left >= max_so_far:
                paid += 1

            max_so_far = max(left, max_so_far)

            queue.popleft()
        else:
            if right >= max_so_far:
                paid += 1

            max_so_far = max(right, max_so_far)

            queue.pop()

    print(f"Case #{i + 1}: {paid}")
