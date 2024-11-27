# age = int(input())
# with_mom = input("Вы с мамой да/нет ") == "да"
# if age > 17 or with_mom:
#     print("Проходи")
# else:
#     print("пшол вон")

# ''
#
# a = [5,7,9]
# print(a)
# a += [5,3,1,6784,5401,239]
# print(a)
# print(a[::-1])

# a='абракaдабра'
# print(a[0:5])
# print(a[::2])
# print(a[:6:-1])
# print(a[::-1])
# print(a[5::-1]+a[10:5:-1])
#
# for i in range(len(a)):
#     print(a[i])
# print()
# c = 0
# for i in range( len(a)):
#     print(a[i+c])
#     c+=1
b =0
a = [13,5,8,11,2,7,9,6]
for i in range(len(a)-1):
    if (a[i]+a[i+1]) %2==0:
        print(a[i],a[i+1])

# a=100
# while True:
#     print(a)
#     a+=1