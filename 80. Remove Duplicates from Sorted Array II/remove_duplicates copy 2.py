def rebuild_message(parts):
    next_part = {}
    prev_part = {}

    for part in parts:
        first_char = part[0]
        next_part[first_char] = part

    for part in parts:
        last_char = part[-1]
        prev_part[last_char] = part

    current_part = next_part["A"]
    result = current_part

    while result[-1] != "Z":
        last_char = result[-1]
        if last_char in next_part:
            next_part_start = next_part[last_char][1:]
            result += next_part_start
        else:
            break

    return result


# Test the function with the given example
parts = ["A---b", "b---c", "c---d", "d---Z"]

print(rebuild_message(parts))
