class bridges():

    def bridges():
        data = []
        with open('day9/input/sample.txt', 'r') as file:
            data = file.readlines()
        for i in range(len(data)):
            data[i] = data[i].strip()
        setVisited = set()
        knots = []
        for i in range(10):
            knots.append([0,0])
        setVisited.add('F' + str(knots[9][0]) + 'S' + str(knots[9][1]))
        for i in data:
            command = i.split()[0]
            move = int(i.split()[1])
            for i in range(move):
                match command:
                    case "R":
                        knots[0][0] += 1
                    case "L":
                        knots[0][0] -= 1
                    case "U":
                        knots[0][1] += 1
                    case "D":
                        knots[0][1] -= 1
                for e in range(1, 10):
                    deltaX = knots[e-1][0] - knots[e][0]
                    deltaY = knots[e-1][1] - knots[e][1]
                    if abs(deltaX) <= 1 and abs(deltaY) <= 1:
                        continue
                    if abs(deltaX) < abs(deltaY):
                        knots[e][0] = knots[e-1][0]
                        knots[e][1] = knots[e-1][1] - deltaY // abs(deltaY)
                    elif abs(deltaX) > abs(deltaY):
                        knots[e][0] = knots[e-1][0] - deltaX // abs(deltaX)
                        knots[e][1] = knots[e-1][1]
                    else:
                        knots[e][0] = knots[e-1][0] - deltaX // abs(deltaX)
                        knots[e][1] = knots[e-1][1] - deltaY // abs(deltaY)
                    if e == 9:
                        setVisited.add('F' + str(knots[e][0]) + 'S' + str(knots[e][1]))
        print(len(setVisited))



    bridges()