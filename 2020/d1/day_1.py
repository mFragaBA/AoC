with open('day_1_input.txt', 'r') as infile:
    lines = infile.read().splitlines();
    numbers = [int(num) for num in lines]

    for num in numbers:
        for num2 in numbers:
            if (num + num2 == 2020):
                print("num: " + str(num))
                print("num2: " + str(num2))
                print(num * num2)
