while True:
    n = int(input())
    if n == -1:
        break
    hour = n // 3600
    n %= 3600
    minute = n // 60
    n %= 60
    print("{:02d}:{:02d}:{:02d}".format(hour, minute, n))
