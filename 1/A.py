a, b = [int(x) for x in input().split()]
x, y = [int(x) for x in input().split()]

trees = {i for i in range(a - b, b + a + 1)} | {i for i in range(x - y, y + x + 1)}

print(len(trees))