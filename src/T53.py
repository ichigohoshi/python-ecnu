def binary_search(num_list: list, value: int) -> int:
    left = 0
    right = len(num_list)-1
    while right > left:
        mid = (left + right) // 2
        if num_list[mid] == value:
            return mid
        elif num_list[mid] > value:
            right = mid - 1
        else:
            left = mid + 1
    return left if num_list[left] == value else -1


n = int(input())
nums = map(int, input().split())
num_list = [i for i in nums]
value = int(input())
position = binary_search(num_list, value)
print(position+1 if position >= 0 else "not found")
