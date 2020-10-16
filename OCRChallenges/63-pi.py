def isEven(num):
    num1 = num / 2
    num2 = num // 2
    if num1 == num2:
        return True
    else:
        return False

# pi = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15)

pi = 0.0

for index, i in enumerate(range(1, 100), start=1):
    thing = (4/((2 * index) - 1))
    if isEven(index):
        pi -= thing
    else:
        pi += thing

print(pi)
