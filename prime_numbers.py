#Zach Moskovitz
#HW 4-1
#prime_numbers.py
#ask the user to give two numbers and the program will find all the
#prime numbers between (and if applicable, including) the numbers given.

#tell the user what te program does
print('This program will give you all the prime numbers between the given\n'
      'starting point and the given end point.')
    
#gather the data from the user
start_num=int(input('What number should we start at? '))
end_num=int(input('What number should we end at? '))

#use a while loop to validate the data given
while start_num<1:
    print('ERROR! You cannot pick a number less than 1 as a starting point!')
    start_num=int(input('What number should we start at? '))
    end_num=int(input('What number should we end at? '))

#use a for loop to determine which numbers are prime number
for num in range(start_num,end_num+1):
    checker=True  #set a boolean variable to determine if num is prime or not
    for prime in range(2,num):
        if (num%prime==0):
            checker=False #if num%prime is not a prime number then it is false
            #and it won't print
    if checker: #if num%prime is a prime number then its true and it will print 
        print(num)
        
            
        
        
                   
