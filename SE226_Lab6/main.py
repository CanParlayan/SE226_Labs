input = int(input("Enter a number:"))
nList = []
x = 1
result = lambda a: (x - 3) / (x * x)
while x <= input:
    nList.append(result(x))
    x = x + 1
print(sum(nList))
y = 1


def generate(a):
    global y
    if a == 0:
        return 1
    else:
        y = y * (a / (a + 2) - 10)
        print(y)
        return y * generate(a - 1)


generate(5)
