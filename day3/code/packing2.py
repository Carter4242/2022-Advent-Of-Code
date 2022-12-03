class Packing():

    def packing():
        data = []
        with open('day3/input/sample.txt', 'r') as file:
            data = file.readlines()
        data = list(map(lambda s: s.strip(), data))
        total = 0
        outputs = []
        groups = []
        for i in range(len(data)):
            if i%3 == 2:
                groups.append(data[i])
                first = groups[0]
                second = groups[1]
                third = groups[2]
                for char in first: 
                    if char in second:
                        if char in third:
                            outputs.append(char)
                            break
                groups = []
            else:
                groups.append(data[i])
        print(outputs)
        for c in outputs:
            if c.islower():
                total += ord(c)-ord("a")+1
            else:
                total += ord(c)-ord("A")+27
        print(total)

    packing()