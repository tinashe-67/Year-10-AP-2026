# Ask the user for the width and loop intil the
# enter a numeber that is more than zero
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

# Main routine goes here

keep_going = ""
while keep_going == "":
    print("Welcome to my area and perimeter calculater.")
    width = num_check("Width of area?: ")

    print()


    height = num_check("Height of area?: ")
   
    perimeter = 2 * (height + width)
    area = height * width
    print(f'area: {area} units')
    print()
    print(f'perimeter: {perimeter} units')

    keep_going = input("Press enter to go again, or any other key to quit")
