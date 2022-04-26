class Module:
    def __init__(self, fun):
        self.fun = fun
        self.children = []


test_case_amount = int(input())
test_cases = []


for _ in range(test_case_amount):
    # We don't need amount of modules
    module_amount = int(input())

    modules = [int(x) for x in input().split(" ")]
    connections = [int(x) for x in input().split(" ")]
    test_cases.append([module_amount, modules, connections])

total_funs = [0 for _ in range(test_case_amount)]


# --------------------------------------------------------------------------------------


def visit(module, total_funs, test_case_number):
    if not module.children:
        return module.fun

    values = [
        visit(
            module=child,
            total_funs=total_funs,
            test_case_number=test_case_number,
        )
        for child in module.children
    ]

    min_value = min(values)
    min_found = 0

    for value in values:
        if not min_found and value == min_value:
            min_found = max(value, module.fun)
        else:
            total_funs[test_case_number] += value

    return min_found


# --------------------------------------------------------------------------------------


for test_case_index, (module_amount, modules, connections) in enumerate(test_cases):
    # print(f"Case #{i + 1}: ", end="")

    # Create module dictionary
    module_map = {}

    # Add abyss as Module
    module_map[0] = Module(0)

    # Create modules
    for j in range(module_amount):
        module_map[j + 1] = Module(modules[j])

    # Create connections
    for j in range(module_amount):
        parent_index = connections[j]

        if module_map.get(j + 1) and module_map.get(parent_index):
            module_map[parent_index].children.append(module_map[j + 1])

    total = visit(module_map[0], total_funs, test_case_index)

    print(f"Case #{test_case_index + 1}:", total_funs[test_case_index] + total)
