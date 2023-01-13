x = ['B', 'v1', 'v2']
formats = input()
for i in formats:
    if i == 'A':
        x[1], x[0] = x[0], x[1]
    elif i == 'B':
        x[2], x[1] = x[1], x[2]
    elif i == 'C':
        x[2], x[0] = x[0], x[2]
for i in range(len(x)):
    if x[i] == 'B':
        print(i+1)