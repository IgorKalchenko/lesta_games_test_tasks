MIN_MERGE_SIZE = 64


def find_minrun(length: int) -> int:
    reminder = 0
    while length >= MIN_MERGE_SIZE:
        reminder |= length & 1
        length >>= 1
    return length + reminder


def insertion_sort(arr: list, left: int, right: int) -> None:
    for i in range(left + 1, right + 1):
        while i > left and arr[i - 1] > arr[i]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1


def merge_sort(arr: list, left: int, middle: int, right: int) -> None:
    length_left = middle - left + 1
    length_right = right - middle
    left_list = [arr[left + i] for i in range(0, length_left)]
    right_list = [arr[middle + i] for i in range(1, length_right + 1)]
    left_i, right_i, total_i = 0, 0, left
    while left_i < length_left and right_i < length_right:
        if left_list[left_i] < right_list[right_i]:
            arr[total_i] = left_list[left_i]
            left_i += 1
        else:
            arr[total_i] = right_list[right_i]
            right_i += 1
        total_i += 1
    while left_i < length_left:
        arr[total_i] = left_list[left_i]
        left_i += 1
        total_i += 1
    while right_i < length_right:
        arr[total_i] = right_list[right_i]
        right_i += 1
        total_i += 1


def tim_sort(arr: list) -> None:
    length = len(arr)
    minrun = find_minrun(length)
    for left in range(0, length, minrun):
        right = min(minrun + left - 1, length - 1)
        insertion_sort(arr, left, right)
    while minrun < length:
        for left in range(0, length, 2 * minrun):
            middle = min(length - 1, minrun + left - 1)
            right = min(length - 1, 2 * length + left - 1)
            if middle < right:
                merge_sort(arr=arr, left=left, middle=middle, right=right)
        minrun *= 2


if __name__ == "__main__":
    user_array: list = list(map(float, input().split()))
    tim_sort(user_array)
    print(user_array)
