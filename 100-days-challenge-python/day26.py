# Recursion in python means calling function inside function body like below example
'''Factorial caluculation 6* 5 = 30 , 30*5 =150 ,150*4 = 600 , 600*3 = 1800 ,1800*2 = 3600
so what we are doing in example factorial of 7 calculation 7 * factorial of 6 = factorial of 7 
'''


# calculate factorial 

# def factorial (x):
#     if(x == 0 or x == 1):
#         return 1
#     else:
#         return x * factorial(x-1)  #factorial of 7 calculation 7 * factorial of 6 = factorial of 7 
    
# print(factorial(5))
'''below is background logic 
5 * factorial(4)
5 * 4 * factorial (3)
5 * 4 * 3 * factorial(2)
5 * 4 * 3 * 2 * factorial (1) now value of 1 is 1 so it will go like this
5 * 4 * 3 * 2 *  = 120 1'''

# quiz : write program for fibbonacci sequence 

def fibonacci (x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2) # x -1 = 6 as x =7 in our case add 7-2=5 so value of 6 will be calculated and the value of 5 and add will get next number
    

''' how this works consider x =7 so F(0)=0 ,F(1)=1 ,f(2)= f(2-1)+f(0) ,f(0) = 0
f(1) = 1
f(2) = f(1) + f(0)
f(3) = f(2) + f(1)
f(4) = f(4-1) + f(4-2)
f(n) = f(n-1) + f(n-2)''' 

print(fibonacci(3))
print(fibonacci(7))
