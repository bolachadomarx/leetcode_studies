from collections import Counter


def calculate_total_cost(items, unit_price):
    # Define the discounts based on the number of items in the set
    discounts = {1: 0.00, 2: 0.10, 3: 0.20, 4: 0.30, 5: 0.40}

    # Count the occurrence of each item
    item_counts = Counter(items)

    total_cost = 0.0

    while item_counts:
        # Create a set with the maximum number of unique items
        current_set = set()
        for item in list(item_counts):
            if len(current_set) < 5:
                current_set.add(item)
                item_counts[item] -= 1
                if item_counts[item] == 0:
                    del item_counts[item]
            else:
                break

        # Calculate the cost for the current set
        set_size = len(current_set)
        discount = discounts[set_size]
        set_cost = (1 - discount) * (set_size * unit_price)
        total_cost += set_cost

    return round(total_cost, 2)


# Example 1
items1 = ["Vanilla", "Banana", "Apple", "Cherry", "Peach", "Banana"]
unit_price1 = 1
print(calculate_total_cost(items1, unit_price1))  # Output should be 4.0

# Example 2
items2 = ["Vanilla", "Apple", "Vanilla", "Apple"]
unit_price2 = 4
print(calculate_total_cost(items2, unit_price2))  # Output should be 14.0

# Example 3
items3 = ["Peach", "Apple", "Vanilla", "Peach"]
unit_price3 = 4
print(calculate_total_cost(items3, unit_price3))  # Output should be 13.0
