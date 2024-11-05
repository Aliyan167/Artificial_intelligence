def hill_height(x):
    return -2 * (x - 5) ** 2 + 20  # Quadratic function with peak at (5, 20)

def hill_climb(start_x):
    current_x = start_x
    current_height = hill_height(current_x)

    while True:
        left_x = current_x - 1
        right_x = current_x + 1
        left_height = hill_height(left_x)
        right_height = hill_height(right_x)

        if left_height > current_height:
            current_x = left_x
            current_height = left_height
        elif right_height > current_height:
            current_x = right_x
            current_height = right_height
        else:
            break

    return current_x, current_height

# Example usage
start_x = 0  # Starting position
final_x, final_height = hill_climb(start_x)
print(f"Hasham and his father Mubarak Said reached the top at x = {final_x} with height = {final_height}")
