def binary_search(arr: list[int], target: int) -> int:
    if target not in arr:
        return -1
    if arr[0] == target:
        return 0
    bottom = 0
    top = len(arr)-1
    while bottom <= top:
        mid = (bottom + top) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            bottom = mid + 1
        else:
            top = mid - 1


if __name__ == "__main__":
    print(binary_search([1, 2, 3, 4, 5], 4))  # Output: 3
    print(binary_search([1, 2], 3))  # Output: -1
