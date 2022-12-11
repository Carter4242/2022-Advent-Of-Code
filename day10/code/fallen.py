class fallen():

    def fallen():
        data = []
        with open('day10/input/sample.txt', 'r') as file:
            data = file.readlines()
        for i in range(len(data)):
            data[i] = data[i].strip()
        cycleNum = 0
        xValue = 1
        importantCycles = []
        for d in data:
            runCycles = 0
            if d == "noop":
                runCycles += 1
            else:
                runCycles += 2
            while(runCycles != 0):
                cycleNum += 1
                if cycleNum in [20, 60, 100, 140, 180, 220]:
                    importantCycles.append(xValue*cycleNum)
                runCycles -= 1
                if (runCycles == 0 and d[0:5] == "addx "):
                    xValue += int(d[5:])
        print(importantCycles)
        print(sum(importantCycles))
    fallen()