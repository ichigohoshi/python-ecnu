def is_palindrome(num: int) -> bool:
    num_str = str(num)
    for i in range(len(num_str)//2):
        if num_str[i] != num_str[len(num_str)-1-i]:
            return False
    return True


n = int(input())
count = 0
while not is_palindrome(n):
    count += 1
    num_reverse_str = str(n)[::-1]
    n += int(num_reverse_str)
print("{:d} {:d}".format(count, n))
