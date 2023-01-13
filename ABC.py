num = [int(item) for item in input().split()]
A, B, C = [m for m in sorted(num)]
order = input()
for i in range(3):
    if order[i] == "A":
        print(A, end=" ")
    elif order[i] == "B":
        print(B, end=" ")
    elif order[i] == "C":
        print(C, end=" ")