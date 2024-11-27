width = int(input())
height = width
for i in range(width):
    stroka = ""
    for j in range(height):
        if i == 0 or i == width-1:
            stroka +="*"
        else:
            if j == 0 or j == height-1:
                stroka +="*"
            if j == i:
                stroka +="*"
            else:
                stroka +=" "
    print(stroka)
