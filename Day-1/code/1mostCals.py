class mostCals():

    def mostCals():
        data = []
        with open('Day-1/input/sample.txt', 'r') as file:
            data = file.readlines()
        print(data)
        totalFoods = []
        lFood = 0
        for food in data:
            if food == "\n":
                totalFoods.append(lFood)
                lFood = 0
            else:
                lFood += int(food.replace('\n', ''))
        totalFoods.append(lFood)
        print(max(totalFoods))



    mostCals()

