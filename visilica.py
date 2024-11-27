import random

f = open('words', 'r', encoding='utf-8')
file = f.readlines()
f.close()
rnd = random.randrange(1,len(file))
slovo = file[rnd]
if rnd == len(file)-1:
    slovo = slovo
else:
    slovo = slovo[:-1]
print('\n' * 100)
slovo_v_zvezdackah = ''
for i in range(len(slovo)):
    slovo_v_zvezdackah+='*'
print(slovo_v_zvezdackah)
hp = 5
pitki = 0
while slovo_v_zvezdackah != slovo and hp > 0:
    vvod = input('Введите букву: ')
    pitki +=1
    if vvod in slovo :
        for i1 in range(len(slovo)):
            if slovo[i1] == vvod:
                past1 = slovo_v_zvezdackah[:i1]
                past2 = slovo_v_zvezdackah[i1+1:]
                slovo_v_zvezdackah = past1 + vvod+ past2
    else:
        print('Чел ты потерал хп')
        hp -= 1

    print(slovo_v_zvezdackah)
    print('У тебя осталось '+str(hp)+' хп')
    if slovo_v_zvezdackah == slovo:
        print('Ты победил за ',pitki,' попыток')

if slovo_v_zvezdackah != slovo:
    print("Ты проиграл слово было",slovo)



