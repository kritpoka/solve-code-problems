x = set()
Mod = 42
for i in range(10):
    x.add(int(input())%Mod)
print(len(x))