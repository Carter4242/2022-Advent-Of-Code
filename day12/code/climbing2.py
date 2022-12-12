class climbing():

    def climbing():
        data = []
        with open('day12/input/sample.txt', 'r') as file:
            data = file.readlines()
        for i in range(len(data)):
            data[i] = data[i].strip()     

        grid = []

        for i in range(len(data)):
            grid.append([])
            for c in data[i]:
                appended = ord(c)-ord('a')
                if appended != -14 and appended != -28:
                    grid[i].append(appended)
                elif appended == -28:
                    grid[i].append(25) 
                else:
                    grid[i].append(0) 
        current = []
        visited = set()  
        for l in range(len(grid)):
            for i in range(len(grid[l])):
                if grid[l][i] == 0:
                    current.append([l, i])
                    visited.add(tuple([l, i]))
        steps = 0
        next = []
        while (True):
            for i in current:
                spot = grid[i[0]][i[1]] # int
                if i[1]-1 != -1:
                    left = grid[i[0]][i[1]-1]
                    if spot+1 >= left:
                        if tuple([i[0],i[1]-1]) not in visited:
                            visited.add(tuple([i[0],i[1]-1]))
                            next.append([i[0],i[1]-1])
                try:
                    right = grid[i[0]][i[1]+1]
                    if spot+1 >= right:
                        if tuple([i[0],i[1]+1]) not in visited:
                            visited.add(tuple([i[0],i[1]+1]))
                            next.append([i[0],i[1]+1])
                except:
                    pass
                if i[0]-1 != -1:
                    top = grid[i[0]-1][i[1]]
                    if spot+1 >= top:
                        if tuple([i[0]-1,i[1]]) not in visited:
                            visited.add(tuple([i[0]-1,i[1]]))
                            next.append([i[0]-1,i[1]])
                try:
                    bottom = grid[i[0]+1][i[1]]
                    if spot+1 >= bottom:
                        if tuple([i[0]+1,i[1]]) not in visited:
                            visited.add(tuple([i[0]+1,i[1]]))
                            next.append([i[0]+1,i[1]])
                except:
                    pass
            steps += 1
            if tuple([20,36]) in visited:
                break
            print(steps)
            current = next.copy()
            next = []
        print(steps)
            

    climbing()