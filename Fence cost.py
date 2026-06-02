def num_check(question):
    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            responce = float(input(question))

            if responce > 0:
                break
                

            else:
                print(error)
                    
        except ValueError:
            print(error)

    return responce

keep_going = ""
while keep_going == "":
    width = num_check("What is the width of the fence: ")
    length = num_check("what is the length of the fence: ")
    perimeter = 2 * (length + width)
    cost_per_m = num_check("What is the cost per meter of fencing: ")
    final_cost = cost_per_m * perimeter
    print()
    print(f'the cost of {perimeter} meters of fencing is ${final_cost}')

    keep_going = input("Press enter to go again, or any other key to quit")

