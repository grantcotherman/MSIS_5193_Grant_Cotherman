#### Iteration and Math with While 
def iteration_math():
    num_list = [1, 2, 4, 5, 6, 7, 9, 10, 13, 14, 15, 16]
    # while loop goes here
    num = 0
    while num < len(num_list):
        if num_list[num] % 2 == 0:
            print("Printing the value", num_list[num], end =" ")
        num += 1
    
iteration_math()

#### Functions and Parameters
def my_function():
    numero = 13
    string1 = 'Oklahoma'
    string2 = 'hats'
    
    # if-else statement here
    if len(string1) != len(string2):
        print("Unequal lengths")
    else:
        print("Equal Lengths")

    # math equation here
    math1 = len(string1) + len(str(numero))
    # print statement here
    print("Math is fun:", math1)
    # return the variable math1
    def mathreturn():
        return(math1)
    mathreturn()
my_function()

#### Lambda Function
def my_lambda():
    string1 = 'Oklahoma'
    string2 = 'hats'
    numero = 13
    t = len(string1) + len(string2) - len(str(numero))
    print(t)
my_lambda()