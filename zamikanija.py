import random
import time


def when_starts(funf):
    def correct_time():
        with open("Vreme", "a") as file:
            file.write(str(funf.__name__) + " runned in " + str(time.time()) + '\n')
            return file

    return correct_time


def times_started(funf):
    times = 0

    def how_many():
        nonlocal times
        times +=1
        print(funf.__name__, " starded ",times," times")
    return how_many


@times_started
def a():
    pass


@times_started
def b():
    pass


@times_started
def c():
    pass


@times_started
def d():
    pass


funcs = [a, b, c, d]
for i in range(random.randint(1, 10)):
    random.choice(funcs)()
