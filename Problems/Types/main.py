# the variable "args" is already defined
my_list = []
for element in args:
    try:
        my_list.append(int(element))
    except:
        pass     
print(my_list)

# further code of the script "process_four_numbers.py"
