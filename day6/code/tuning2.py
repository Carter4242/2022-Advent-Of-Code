class tuning():

    def tuning():
        data = []
        with open('day6/input/sample.txt', 'r') as file:
            data = file.readlines()
        for i in range(len(data)):
            data[i] = data[i].strip()
        data = data[0]
        for i in range(13, len(data)):
            word = data[i-13: i+1]
            num = 0
            for c in word:
                if word.count(c) != 1:
                    break
                num += 1
            if num == 14:
                print(word)
                print(i+1)
                break

    tuning()