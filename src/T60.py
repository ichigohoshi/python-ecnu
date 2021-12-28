def calculate() -> float:
    global str_stack
    ch = str_stack.pop()
    if ch == '+':
        return calculate() + calculate()
    elif ch == '-':
        return calculate() - calculate()
    elif ch == '*':
        return calculate() * calculate()
    elif ch == '/':
        return calculate() / calculate()
    else:
        return float(ch)


words = map(str, input().split())
str_stack = [word for word in words][::-1]
print("{:.6f}".format(calculate()))
