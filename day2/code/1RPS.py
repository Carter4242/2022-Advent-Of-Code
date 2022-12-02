class run():

    def run():
        data = []
        with open('day2/input/sample.txt', 'r') as file:
            data = file.readlines()

        score = 0
        for game in data:
            them = game[0]
            you = game[2]
            win = ord(you)-ord("X")+1
            score += win
            if them == "A":
                if you == "Y":
                    score += 6
                if you == "X":
                    score += 3
            if them == "B":
                if you == "Y":
                    score += 3
                if you == "Z":
                    score += 6
            if them == "C":
                if you == "Z":
                    score += 3
                if you == "X":
                    score += 6
        print(score)
            


    run()

    # .replace('\n', '')