# write a program that reads in 10 numbers, then prints the sum of those

my_number = 0
index = 0
print("Enter 10 numbers")
while index < 10:
    index += 1
    my_input = int(input("Enter number\n"))
    my_number += my_input
print("Those numbers make:", my_number)