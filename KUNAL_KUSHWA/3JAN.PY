#### STORE A COLLECTION OF DIFFERENT ROLL NUMBERS #########
# boss = list(range(0,15))

# print (boss)

############# Input a year and find whether it is a leap year or not. ############

# year = int(input('enter the year'))
# print(year)
# if year % 4 ==0 :
#     print('leap year')
    
# else:
#     print('not a leap year')

########## Take two numbers and print the sum of both. #######

# num1 = int(input('enter the numbers'))
# num2 = int(input('enter the numbers'))

# print(num1+num2)

######### Take a number as input and print the multiplication table for it. ###########

# mul = int(input('enter the number'))
# len = int(input('enter the length'))
# for i in range(1,len+1):
#     print(mul,'*',i ,'=',mul*i)


######### Take 2 numbers as inputs and find their HCF and LCM ##########

num1 = int(input('enter the first number'))
num2 = int(input('enter the second number'))

k = min(num1,num2)
l = max(num1,num2)

if l % k == 0:
    print('hcf is ',k)
    
else:
    list=[]
    for i in range(1,k+1):
        list.reverse()
        if k % i ==0:
            list + i
    for i in list:
        if l % i == 0:
            print('hcf',list[i])
          
        
               