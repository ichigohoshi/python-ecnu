n = int(input())
for times in range(n):
    person_sum, money_sum = map(int, input().split())
    print("case #{:d}:".format(times))
    if person_sum * 3 < money_sum or person_sum > money_sum:
        print(-1)
    else:
        for i in range(person_sum+1):
            for j in range(person_sum+1-i):
                k = person_sum-i-j
                if i * 3 + j * 2 + k == money_sum:
                    print("{:d} {:d} {:d}".format(i, j, k))
