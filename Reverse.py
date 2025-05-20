def reverse_digits(number):
    """
    Reverses the digits of a number.

    Args:
        number (int): The number to reverse.

    Returns:
        int: The number with its digits reversed.
    """
    sign = 1 if number >= 0 else -1  # Store the sign
    number = abs(number)             # Work with the absolute value

    reversed_number = 0
    while number > 0:
        reversed_number = (reversed_number * 10) + (number % 10)
        number //= 10  # Integer division to remove the last digit

    return sign * reversed_number


# Example usage:
num1 = 45
num2 = -123
num3 = 67890

print(reverse_digits(num1))  # Output: 54
print(reverse_digits(num2))  # Output: -321
print(reverse_digits(num3))  # Output: 9876
