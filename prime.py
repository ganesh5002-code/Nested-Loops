# Take input from user for two numbers
lower = int(input("Enter a number")) 
upper = int(input("Enter another number way more than your first number"))

for num in range(lower,upper+1):
    if num>1:
        for x in range(2,num):
            if num % x == 0:
                break
        else:
            print("The prime numbers between", lower, "and", upper, "are:\n",num)