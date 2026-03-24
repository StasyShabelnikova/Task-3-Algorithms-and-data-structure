def feed_animals(animals, food):
    if len(animals) == 0 or len(food)== 0:
        return 0
    animals.sort()
    food.sort()
    count = 0
    for f in food:
        if  count < len(animals) and f >= animals[count]:
            count += 1
    return count