def binary_search(nums, num, left, right):
    mid = (left + right) // 2
    if left > right:
        return -1
    if num == nums[mid]:
        return mid
    elif num > nums[mid]:
        left = mid + 1
    else:
        right = mid - 1
    return binary_search(nums, num, left, right)


n = int(input())
nums_seq = map(int, input().split())
nums = []
for i in nums_seq:
    nums.append(i)
num = int(input())
print(binary_search(nums, num, 0, n-1))
