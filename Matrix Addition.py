m,n = [int(e) for e in input().split()]
x = []
for i in range(2*m):
    y = [int(e) for e in input().split()]
    x.append(y)
for i in range(m):
    for j in range(n):
        x[i][j] += x[i+m][j]
x = x[:m]
for e in x:
    f = [str(integer) for integer in e]
    a_string = " ".join(f)
    print(a_string)