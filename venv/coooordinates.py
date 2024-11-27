coordinates = [5, 3]
instrutions = ["left", "up", "up", "right","right"]
rastoinoe = 0
for i in instrutions:
    if i == "up":
        coordinates[1] += 1
        rastoinoe += 1
    if i == "down":
        coordinates[1] -= 1
        rastoinoe += 1
    if i == "left":
        coordinates[0] -= 1
        rastoinoe += 1
    if i == "right":
        coordinates[0] += 1
        rastoinoe += 1
print(str(coordinates[0])+",",coordinates[1])
print(rastoinoe)

