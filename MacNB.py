a = [1,2,3,8,9]
b = [4,5,6]
otvet = []
for i in range(len(a)):
    otvet.append(a[i])
    otvet.append(b[i])
    if len(a)> len(b):
        for i in range(len(b)-len(a)):
            otvet.append(b[i+len(a)])
    elif len(b)> len(a):
        for i in range(len(a)-len(b)):
            otvet.append(a[i+len(b)])
for i in range(len(otvet)):
    print(otvet[i])