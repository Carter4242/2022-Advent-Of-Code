class bridges():

    def bridges():
        data = []
        with open('day9/input/sample.txt', 'r') as file:
            data = file.readlines()
        for i in range(len(data)):
            data[i] = data[i].strip()
        setVisited = set()
        head = [0,0]
        tail = [0,0]
        setVisited.add('F' + str(tail[0]) + 'S' + str(tail[1]))
        for i in data:
            command = i.split()[0]
            move = int(i.split()[1])
            for i in range(move):
                match command:
                    case "R":
                        head[0] += 1
                    case "L":
                        head[0] -= 1
                    case "U":
                        head[1] += 1
                    case "D":
                        head[1] -= 1
                deltaX = head[0] - tail[0]
                deltaY = head[1] - tail[1]
                if abs(deltaX) <= 1 and abs(deltaY) <= 1:
                    continue
                if abs(deltaX) < abs(deltaY):
                    tail[0] = head[0]
                    tail[1] = head[1] - deltaY // abs(deltaY)
                elif abs(deltaX) > abs(deltaY):
                    tail[0] = head[0] - deltaX // abs(deltaX)
                    tail[1] = head[1]
                else:
                    tail[0] = head[0] - deltaX // abs(deltaX)
                    tail[1] = head[1] - deltaY // abs(deltaY)
                setVisited.add('F' + str(tail[0]) + 'S' + str(tail[1]))
        print(len(setVisited))



        

    bridges()