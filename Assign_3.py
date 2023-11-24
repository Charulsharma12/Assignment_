#Write a Python function to sum all the numbers in a list.
#Write the numbers in a list 
a = input("Enter the numbers of a list:")
#a is a string 
b = list(a)
#b is a list
def sum_numbers(input_list): 
    sum = 0

    for i in range(len(input_list)):
        sum = sum + int(input_list[i])
#int function to change the numbers of input list in int format
              
    return sum 
print("Sum of the numbers given:",sum_numbers(b))

#if the function takes the list where the numbers are in int/float format 

def sum_numbers_in_list(list):
    sum_numbers = 0 
    for i in range(len(list)):
      sum_numbers = sum_numbers + list[i]
    return sum_numbers

print(sum_numbers_in_list([1,2,3,4,5]))