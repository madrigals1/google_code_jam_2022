class Customer:
    def __init__(self, products):
        self.products = products

        self.min_product = min(self.products)
        self.max_product = max(self.products)

        # Left to Right (Direction)
        self.ltr = True
        self.presses = self.max_product - self.min_product

    def __str__(self):
        return f"Customer: {self.min_product}, {self.max_product}, {self.ltr}"

    # return self.ltr, other.ltr
    def get_ltr(self, other_customer):
        if self.ltr:

            diff_min = abs(self.max_product - other_customer.min_product)
            diff_max = abs(self.max_product - other_customer.max_product)

            return diff_min <= diff_max

        else:

            diff_min = abs(self.min_product - other_customer.min_product)
            diff_max = abs(self.min_product - other_customer.max_product)

            return diff_min <= diff_max


def get_ltr(first, second, third):
    if first.ltr:

        diff_min = abs(first.max_product - second.min_product)
        diff_max = abs(first.max_product - second.max_product)

        return diff_min <= diff_max

    else:

        diff_min = abs(first.min_product - second.min_product)
        diff_max = abs(first.min_product - second.max_product)

        return diff_min <= diff_max


test_case_amount = int(input())
test_cases = []

for _ in range(test_case_amount):
    num_customers, num_products, *_ = [int(x) for x in input().split(" ")]

    customers = []

    for _ in range(num_customers):
        products = [int(x) for x in input().split(" ")]
        customers.append(Customer(products))

    test_cases.append(customers)

for i, customers in enumerate(test_cases):

    j = 0

    # Add presses for first Customer
    presses = customers[0].max_product
    last_pressure = customers[0].max_product

    while j < len(customers) - 1:
        curr_customer = customers[j]
        next_customer = customers[j + 1]

        next_customer.ltr = curr_customer.get_ltr(next_customer)

        j += 1

    while j > 1:
        curr_customer = customers[j]
        next_customer = customers[j - 1]

        next_customer.ltr = curr_customer.get_ltr(next_customer)

        j -= 1

    [print(customer) for customer in customers]

    for customer in customers[1:]:

        if customer.ltr:
            presses += abs(last_pressure - customer.min_product)
            presses += customer.presses
            last_pressure = customer.max_product
        else:
            presses += abs(last_pressure - customer.max_product)
            presses += customer.presses
            last_pressure = customer.min_product

    print(f"Case #{i + 1}: {presses}")
