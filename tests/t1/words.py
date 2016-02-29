# Write a program to read in words from the keyboard one at a time until the word "quit" is typed.
# Store them in a list then print them alphabetically

my_list = []
my_input = input("Enter words. This will sort them until you type quit.\n")
while my_input != "quit":
    my_list.append(my_input)
    my_input = input("Enter words. This will sort them until you type quit.\n")
my_list.sort()
print(my_list)