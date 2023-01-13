lists = []
for i in range(9):
    lists.append(int(input()))
more_than_100 = sum(lists)-100
for a in lists:
    for b in lists:
        if more_than_100 == a+b and a != b:
            lists.remove(a)
            lists.remove(b)
for i in lists:
    print(i)
