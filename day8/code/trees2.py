class trees():

    def trees():
        data = []
        with open('day8/input/sample.txt', 'r') as file:
            data = file.readlines()
        for i in range(len(data)):
            data[i] = data[i].strip()
        bestScore = 0
        for i in range(len(data)):
            for c in range(len(data[i])):
                height = int(data[i][c])
                left = data[i][0:c]           
                right = data[i][c+1:len(data[i])]
                top = ""
                bottom = ""
                for y in range(i-1, -1, -1):
                    top += data[y][c]
                for y in range(i+1, len(data)):
                    bottom += data[y][c]
                scenicLeft = 0
                scenicRight = 0
                scenicTop = 0
                scenicBottom = 0
                for c in left[::-1]:
                    scenicLeft+=1
                    if int(c) >= height:
                        break    
                for c in right:
                    scenicRight+=1
                    if int(c) >= height:
                        break
                for c in top:
                    scenicTop+=1
                    if int(c) >= height:
                        break
                for c in bottom:
                    scenicBottom+=1
                    if int(c) >= height:
                        break
                if scenicLeft * scenicRight * scenicTop * scenicBottom > bestScore:
                    bestScore = scenicLeft * scenicRight * scenicTop * scenicBottom
        print(bestScore)
        

    trees()