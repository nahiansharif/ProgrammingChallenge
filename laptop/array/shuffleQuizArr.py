import random as rnd

with open('quizArray.txt', 'r') as txtfile:
    lines = []
    for line in txtfile:
        lines.append(line)
    lst = lines.copy()

    rnd.shuffle(lines) 
    i = 0
    shuffledQUiz = []
    for line in lines:
        if line != "":
            i += 1
            shuffledQUiz.append("q" + str(i) + ": " + line + "\n")

    with open("shuffle_quiz_array.txt", "w") as file2:
        for row in shuffledQUiz:
            file2.write("".join(map(str, row)))

        

