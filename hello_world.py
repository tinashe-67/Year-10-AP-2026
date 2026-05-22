greeting = "hello world"
print(greeting)

number1 = 7 
number2 = 5

sum = number1 + number2
print(sum)

like_coffee = input("do you like coffee?")


if like_coffee == "yes":
    print("That is great! I like coffe too!")

elif like_coffee == "no":
    print("I dont like coffe either! Im might try sometime")

else:
    print("This isn't the answer im looking for" )

    keep_going = input("Pres <enter> to continue or any other key to quit")

print("All done")

num_1 = int(input("Please enter your first number: "))
num_2 = int(input("Please enter your first number: "))

sum = num_1 + num_2

print(f"The answer to your to the sum of your numbers is {sum}")