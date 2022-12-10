class cleanup():

    def cleanup():
        data = []
        with open('day4/input/sample.txt', 'r') as file:
            data = file.readlines()
        for i in range(len(data)):
            data[i] = data[i].strip().split(',')
        total = 0
        for item in data:
            one = int(item[0].split('-')[0])
            two = int(item[0].split('-')[1])
            three = int(item[1].split('-')[0])
            four = int(item[1].split('-')[1])
            if (three <= one <= four or three <= two <= four) or (one <= three <= two or one <= four <= two):
                # print(one, two, three, four)
                total += 1
        print(total)



        
    cleanup()