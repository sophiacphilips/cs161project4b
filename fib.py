#Author: Sophia Philips
#GitHub Username: sophiacphilips
#Date: 10/19/2022
#This code takes an integer and find its place in the fibonacci sequence.

#define def fib and variables that will be used to place location of numbers
def fib(num):
    x=0
    y=1
    if num==0:
        return x
    elif num==1:
        return y
#set fib equation
    else:
        for i in range(2,num+1):
            z=x+y
            x=y
            y=z
        return y

#ex of call and print
#term=fib(17)
#print(term)
