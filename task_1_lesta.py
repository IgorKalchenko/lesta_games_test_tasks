def is_even_first(value: int) -> bool:
    return not value & 1


if __name__ == "__main__":
    val: int = int(input())
    print(is_even_first(val))
