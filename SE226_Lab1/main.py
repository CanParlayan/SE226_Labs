name = str(input("What is your name?"))
print("Hello " + name)
ID = str(input("What is your student ID"))
print("Your ID is " + ID)

number1 = int(input("Enter a number."))
number2 = int(input("Enter another number."))
sum = int(number1 + number2)
diff = int(number1 - number2)
prod = int(number1 * number2)
print("Summation of the numbers is " + str(sum))
print("Difference of the numbers is " + str(diff))
print("Product of the numbers is " + str(prod))

for i in range(0, 3):
    for j in range(0, i+1):
        print("*", end='')
    print("\r")

