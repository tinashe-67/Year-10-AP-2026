keep_going = ""
while keep_going == "":
    width = float(input("What is the width of the fence: "))
    length = float(input("what is the length of the fence: "))
    perimeter = 2 * (length + width)
    cost_per_m = int(input("What is the cost per meter of fencing: "))
    final_cost = cost_per_m * perimeter
    print()
    print(f'the cost of {perimeter} meters of fencing is ${final_cost}0')

    keep_going = input("Press enter to go again, or any other key to quit")
