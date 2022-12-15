class distress():

    def distress(self):
        data = []
        with open('day13/input/sample.txt', 'r') as file:
            data = file.readlines()
        for i in range(len(data)):
            data[i] = data[i].strip()

        data = list(filter(None, data))
        
        packets = []

        for i in data:
            packets.append(list(eval(i)))
        
        total = 0

        for i in range(0, len(packets), 2):
            left = packets[i]
            right = packets[i+1]
            
            if 0 > self.compareList(left, right):
                total += (i//2)+1

        print(total)
    

    def compareList(self, left, right) -> int:
        if isinstance(left, int) and isinstance(right, int):
            return left - right

        if isinstance(left, int) and not isinstance(right, int):
            return self.compareList([left], right)
        
        if not isinstance(left, int) and isinstance(right, int):
            return self.compareList(left, [right])
        
        for l, r in zip(left, right):
            difference = self.compareList(l, r)
            if difference != 0:
                return difference
        return len(left) - len(right)




distressCompare = distress()
distress.distress(distressCompare)