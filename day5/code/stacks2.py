class stacks():

    def stacks():
        data = []
        with open('day5/input/sample.txt', 'r') as file:
            data = file.readlines()
        for i in range(len(data)):
            data[i] = data[i].strip('\n')
        stacks = []
        for i in range(1, 37, 4):
            stacks.append([])
        stackNum = 0
        for i in range(7, -1, -1):
            for e in range(1, 37, 4):
                if data[i][e] != ' ':
                    stacks[stackNum].append(data[i][e])
                stackNum += 1
            stackNum = 0
        for i in range(10, len(data)):
            before = data[i].split(" from")[0]
            after = data[i].split(" from")[1]
            numCrates = int(before[5:])
            fromStack = int(after[1])-1
            toStack = int(after[6])-1
            changeStack = []
            for i in range(numCrates):
                changeStack.append(stacks[fromStack].pop())
            changeStack.reverse()
            for i in changeStack:
                stacks[toStack].append(i)

        output = ""
        for stack in stacks:
            output += stack[-1]
        print(output)
            

    stacks()