import random
import time
total = 0
numer = []

with open("Chifri", "r") as file:
    for i in range(700000):
        numer.append(float(file.readline()[:-1]))
for j in range(100):
    start = time.time()
    a = max(numer)
    b = min(numer)
    # min(numer)
    # max_n = 0
    # min_n = 5000
    # for number in numer:
    #     if number > max_n:
    #         max_n = number
    #     if number < min_n:
    #         min_n = number
    total += time.time() - start
print(total/100)

