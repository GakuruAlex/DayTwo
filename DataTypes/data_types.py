def add_digits(number: str) -> int:
    """_summary_

    Args:
        number (str): _Input from user_

    Returns:
        sum: _Sum of the two digits of the number_
    """
    if number.startswith("-"):
        number = [int(x) for x in number[1:]]
        return sum(number)
    else:
        return sum([int(x) for x in number ])

def main()->None:

    two_digit_number = input("")
    print(f"The sum of digits of {two_digit_number} is: {add_digits(two_digit_number)}")

if __name__ == "__main__":
    main()

