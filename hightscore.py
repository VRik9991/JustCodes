choice = int(input(">Press 1 to add\n>Press 2 to erase\n>What are you want to do\n>"))
with open("highscores.txt", 'r') as file:
    scores = file.readlines()
    new_score = input()
    scores.append(new_score)
    split_new_score = new_score.split()
    split_new_score[2] = int(split_new_score[2])
    display_score = []
    for i in range(len(scores)):
        sorter = scores[i].split()
        sorter[2] = int(sorter[2])
        scores[i] = sorter
    # print(scores)
    scores = sorted(scores, key=lambda X: X[2])
    if choice == 2:
        scores.remove(split_new_score)
        print("done")
    if choice == 1:
        for i in range(len(scores) - 1, 0, -1):
            if scores[i][1] == split_new_score[1]:
                display_score.append(scores[i])
        display_score = sorted(display_score, key=lambda X: X[2])
        for i in range(len(display_score) - 1, 0, -1):
            print(display_score[i][0], display_score[i][1], display_score[i][2])
with open("highscores.txt", "w") as file:
    strcore = ""
    for scork in scores:
        strcore += f"{scork[0]} {scork[1]} {scork[2]}\n"
    file.write(strcore)
