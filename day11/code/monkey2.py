import math

class monkey():
    def monkey():
        data = []
        with open('day11/input/sample.txt', 'r') as file:
            data = file.readlines()
        for i in range(len(data)):
            data[i] = data[i].strip()
        monkeys = [
        [[63, 57], ['*'], [11], [7, 6, 2], [0]]
        ,[[82, 66, 87, 78, 77, 92, 83], ['+'], [1], [11, 5, 0], [0]]
        ,[[97, 53, 53, 85, 58, 54], ['*'], [7], [13, 4, 3], [0]]
        ,[[50], ['+'], [3], [3, 1, 7], [0]]
        ,[[64, 69, 52, 65, 73], ['+'], [6], [17, 3, 7], [0]]
        ,[[57, 91, 65], ['+'], [5], [2, 0, 6], [0]]
        ,[[67, 91, 84, 78, 60, 69, 99, 83], ['^'], [0], [5, 2, 4], [0]]
        ,[[58, 78, 69, 65], ['+'], [7], [19, 5, 1], [0]]
        ]
        roundDown = math.lcm(*[monkey[3][0] for monkey in monkeys])
        for l in range(10000):
            for i in range(len(monkeys)):
                for e in range(len(monkeys[i][0])):
                    monkeys[i][4][0] += 1
                    if monkeys[i][1][0] == '*':
                        monkeys[i][0][e] = (monkeys[i][0][e]*monkeys[i][2][0])%roundDown
                    elif monkeys[i][1][0] == '+':
                        monkeys[i][0][e] = (monkeys[i][0][e]+monkeys[i][2][0])%roundDown
                    elif monkeys[i][1][0] == '^':
                        monkeys[i][0][e] = (monkeys[i][0][e]*monkeys[i][0][e])%roundDown
                    if monkeys[i][0][e]%monkeys[i][3][0] == 0:
                        monkeys[monkeys[i][3][1]][0].append(monkeys[i][0][e])
                    else:
                        monkeys[monkeys[i][3][2]][0].append(monkeys[i][0][e])
                monkeys[i][0] = []
        totals = []
        for i in monkeys:
            totals.append(i[4][0])
        first = max(totals)
        totals.remove(first)
        print(max(totals)*first)
            

    monkey()