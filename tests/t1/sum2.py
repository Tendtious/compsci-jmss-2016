# copy the code from sum1.py into this file, THEN:
# change your program so it keeps reading numbers until it gets a -1, then prints the sum of all numbers read

my_number = 0
my_input = 0
print("Enter numbers. This will end on a -1")
while my_input != -1:
    my_number += my_input
    my_input = int(input("Enter number\n"))
print("Those numbers make:", my_number)