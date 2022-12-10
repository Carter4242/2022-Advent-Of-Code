class dir:

    size = 0

    def __init__(self, parent=None):
        self.parent = parent
        self.children = dict()
    
    def totalSize(self):
        for child in self.children.values():
            child.totalSize()
            self.size += child.size

class noStorage():

    def noStorage():
        data = []
        with open('day7/input/sample.txt', 'r') as file:
            data = file.readlines()
        for i in range(len(data)):
            data[i] = data[i].strip()
        data.pop(0)
        root = cd = dir()
        dirs = [root]
        for line in data:
            if line[0:4] == ("$ ls"):
                pass
            elif line[0:] == "$ cd ..":
                cd = cd.parent
            elif line[0:4] == ("$ cd"):
                cd = cd.children[line[5:]]
            elif line[0:4] == ("dir "):
                d = cd.children[line[4:]] = dir(cd)
                dirs.append(d)
            else:
                cd.size += int(line.split()[0])

        root.totalSize()

        print(sum(dir.size for dir in dirs if dir.size <= 100000))            

    noStorage()
