max_calories = 0
with open('../inputs/01.txt') as f:
    lines = f.readlines()
    calorie_counter = 0
    for line in lines:
        if line == '\n':
            if calorie_counter > max_calories:
                max_calories = calorie_counter
            calorie_counter = 0
        else:
            calorie_counter += int(line)

    print(max_calories)
