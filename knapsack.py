class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.value_per_unit = value / weight  # Value per unit weight

def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x.value_per_unit, reverse=True)

    total_value = 0.0
    knapsack = [0.0] * len(items)

    for i, item in enumerate(items):
        if capacity >= item.weight:
            knapsack[i] = 1.0
            total_value += item.value
            capacity -= item.weight
        else:
            fraction = capacity / item.weight
            knapsack[i] = fraction
            total_value += fraction * item.value
            break

    return total_value, knapsack

# Example Usage:
items = [Item(10, 60), Item(20, 100), Item(30, 120)]
knapsack_capacity = 50

total_val, knapsack_contents = fractional_knapsack(items, knapsack_capacity)
print(f"Total value in knapsack: {total_val}")
print("Knapsack contents (fraction taken for each item):", knapsack_contents)
