numberInput = int(input("What number would you like to see? "))
print(numberInput)
my_file = open("fizzbuzz.txt", "+w")
def function1():
     for number1 in range (1, numberInput):
         if (number1 % 5 == 0) and (number1 % 3 == 0):
             my_file.write(str(number1) + "\n")
             print("FIZZBUZZ")
         elif (number1 % 3 == 0):
             print("Fizz")
         elif (number1 % 5 == 0):
             print ("Buzz")
         else:
             print(number1)
function1()