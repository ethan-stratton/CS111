#Requests that the user enter a string and stores the user's response in a variable.
#Reverses the order of the string; for example, the string "Catastrophe!" should become "!ehportsataC".
#Creates and displays for the user a new string that includes only every second letter from the 
#reversed string. For example, if the user entered "Catastrophe!" the final output should be "!hotaa".

# Ask the user to input a string
user_input = input("Please enter a word or phrase: ")

# Reverse the order of the characters in the input string
reversed_input = ''.join(reversed(user_input))

# Create a new string that includes every second letter from the reversed input string
every_second_letter = ""
for i in range(len(user_input)):
    if i % 2 != 0:
        every_second_letter += user_input[i]

# Display the new string to the user
print("Here's the result: ", reversed_input)
print("Here's the result: ", every_second_letter)

#Defines a function named MyCoolFunction that accepts two parameters named x and y. 
#When called, MyCoolFunction should return the value 2*x + y - 1.
#Defines two variables named A and B, then calls MyCoolFunction on A and B and 
#stores the result in a new variable named C.
#Returns the result of calling MyCoolFunction on A and C. When A=5 and B=0, 
#the result of running your program should be 18.

# Define the function MyCoolFunction
def MyCoolFunction(x, y):
    return 2 * x + y - 1

# Define variables A and B
A = 5
B = 0

# Call MyCoolFunction on A and B, store the result in C
C = MyCoolFunction(A, B)

# Return the result of calling MyCoolFunction on A and C
result = MyCoolFunction(A, C)
print(result)


#Using a programming language and development environment of your choice, write a program that will 
#calculate the area of an arbitrary shape (circle, triangle, square, or rectangle) given the necessary 
#radius or side length(s). You may choose whether the shape type and radius/side length(s) are hard-coded 
#as a variable at the top of your code, or whether the system will prompt the user for the needed values 
#one at a time.

#If the shape to be calculated is a circle, the calculated area should be A=pi*radius*radius. 
#For a triangle, A=1/2*length*height. For a square, A=length*length. For a rectangle, A=width*height.


def calculate_square_area(side_length):
    return side_length ** 2

side_length = float(input("Enter the side length of the square: "))
area = calculate_square_area(side_length)
print("The area of the square is:", area)
