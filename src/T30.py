num = -1


def add_n(n):
    global num
    num += n
    print(num)


def cycle_m(m, n):
    for j in range(m):
        add_n(n)


def cycle_o(m, n, o):
    add_n(o)
    cycle_m(m, n)


def cycle_p():
    for j in range(8):
        cycle_o(9, 11, 2)


def cycle_q(q):
    for j in range(q):
        cycle_p()
        cycle_o(8, 11, 2)
        cycle_o(8, 11, 15)


def cycle_r():
    for j in range(8):
        cycle_o(9, 11, 2)
    cycle_o(7, 11, 2)
    cycle_o(7, 11, 28)


def cycle_s(s):
    for j in range(9):
        cycle_q(9)
        cycle_r()
    cycle_q(9)
    cycle_p()
    cycle_o(s, 11, 2)


cycle_m(5, 2)
cycle_m(9, 11)
for i in range(9):
    cycle_s(6)
    cycle_o(6, 11, 41)
cycle_s(5)
