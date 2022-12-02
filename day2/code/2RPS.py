class run():

    def run():
        data = []
        with open('day2/input/sample.txt', 'r') as file:
            data = file.readlines()

        score = 0
        for game in data:
            them = game[0]
            you = game[2]
            points = 1
            if them == "C":
                points = 3
            if them == "B":
                points = 2
            if you == "Y":
                score += 3
                score += points
            if you == "Z":
                score += 6
                if (points+1)%3 == 0:
                    score += 3
                else:
                    score += (points+1)%3
            if you == "X":
                if (points-1)%3 == 0:
                    score += 3
                else:
                    score+= (points-1)%3


        print(score)
            


    run()

    # .replace('\n', '')