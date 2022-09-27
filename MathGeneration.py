import time

x = -8
print(x)
x = -(x ** 3)
print("= "+ str(x))
x = -(x ** (1/3))
x = round(x)

time.sleep(0.5)

while 1 == 1:
    y = round(x)
    y = y - 10
    print(y)
    y = -(y ** 3)
    y = round(y)
    print("= " + str(y))
    y = -(y ** (1/3))
    y = round(y)

    time.sleep(0.5)

    x = round(y)
    x = x - 10
    print(x)
    x = -(x ** 3)
    x = round(x)
    print("= " + str(x))
    x = -(x ** (1/3))
    x = round(x)

    time.sleep(0.5)

