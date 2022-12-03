class Packing():

    def packing():
        data = []
        with open('day3/input/sample.txt', 'r') as file:
            data = file.readlines()
        data = map(lambda s: s.strip(), data)
        total = 0
        outputs = []
        for rucksack in data:
            first = rucksack[0:len(rucksack)//2]
            second = rucksack[len(rucksack)//2:]
            for char in first: 
                if char in second: 
                    outputs.append(char)
                    break
        print(outputs)
        for c in outputs:
            if c.islower():
                total += ord(c)-ord("a")+1
            else:
                total += ord(c)-ord("A")+27
        print(total)

    packing()