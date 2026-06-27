def reverse_number(num):
    """Return the digits of an integer reversed.

    Args:
        num (int): The integer to reverse.

    Returns:
        int: The reversed integer, preserving sign.
    """
    sign = -1 if num < 0 else 1
    reversed_str = str(abs(num))[::-1]
    return sign * int(reversed_str)


def is_palindrome_number(num):
    """Check whether an integer is a palindrome.

    Args:
        num (int): The integer to check.

    Returns:
        bool: True if num is a palindrome, False otherwise.
    """
    return num >= 0 and num == reverse_number(num)


def main():
    try:
        num = int(input("Enter an integer: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    reversed_num = reverse_number(num)
    print(f"Reversed number: {reversed_num}")

    if is_palindrome_number(num):
        print("This number is a palindrome.")
    else:
        print("This number is not a palindrome.")


if __name__ == "__main__":
    main()