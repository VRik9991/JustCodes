import random

word = input()
lenword = len(word)
total_probels = 0
for i in range(1,lenword):
    rnd = random.randint(1,5)
    word = word[:i+total_probels] +" "*rnd + word[i+total_probels:]
    total_probels += rnd
print(word)