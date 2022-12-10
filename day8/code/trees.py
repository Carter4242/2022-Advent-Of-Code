class trees():

    def trees():
        data = []
        with open('day8/input/sample.txt', 'r') as file:
            data = file.readlines()
        for i in range(len(data)):
            data[i] = data[i].strip()
        totalVisible = 0
        notVisible = 0
        for i in range(len(data)):
            for c in range(len(data[i])):
                left = data[i][0:c]           
                right = data[i][c+1:len(data[i])]
                top = ""
                bottom = ""
                for y in range(i-1, -1, -1):
                    top += data[y][c]
                for y in range(i+1, len(data)):
                    bottom += data[y][c]
                invisibleLeft = False
                invisibleRight = False
                invisibleTop = False
                invisibleBottom = False
                for x in range(int(data[i][c]), 10):
                    if left.count(str(x)) != 0:
                        invisibleLeft = True
                        break     
                for x in range(int(data[i][c]), 10):
                    if right.count(str(x)) != 0:
                        invisibleRight = True
                        break
                for x in range(int(data[i][c]), 10):
                    if top.count(str(x)) != 0:
                        invisibleTop = True
                        break
                for x in range(int(data[i][c]), 10):
                    if bottom.count(str(x)) != 0:
                        invisibleBottom = True
                        break      
                if not (invisibleLeft and invisibleRight and invisibleTop and invisibleBottom):
                    totalVisible += 1
                else:
                    notVisible += 1
        print(totalVisible, notVisible)
        

    trees()