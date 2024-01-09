def is_even_first(value: int) -> bool:
    """
    Function that defines if number is even.
    Accepts integer type value.
    Returns boolean type answer:
    If True value is even, if false value is odd.
    """
    return not value & 1


if __name__ == "__main__":
    val: int = int(input())
    print(is_even_first(val))
