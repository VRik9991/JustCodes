numer = int(input())
otv = 0
otvet = ""
coppy_of_i = 0
for i in range(numer-1):
    otv += (i+1)*(i+2)
    coppy_of_i = i+2
    otvet += str(i+1) + " * " + str(coppy_of_i)
    if i+1 != numer-1:
        otvet += " + "
otvet += " ="
print(otvet,otv)