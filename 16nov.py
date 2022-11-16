# swapping two numbers using addition and sun..
# a=int(input("enter 1st"))
# b=int(input("enter 2nd"))

# a=a+b
# b=a-b
# a=a-b
# print(a,b)
##############
#using mult. and div.

# a=int(input("enter 1st"))
# b=int(input("enter 2nd"))

# a=a*b
# b=a/b
# a=a/b
# print(a,b)

########################
#GIVE THE NUMBER OF ITEMS TO BE SWAPPED AND THEN SWAP THE TWO NUMBERS ENTERED

# r=int(input('enter range'))
# i=0
# while i< r:
#         a=int(input('enter first number'))
#         b=int(input('enter second number'))
#         a,b = b,a
#         print(a,b)
#         i+=1

###############################################

#BINARY SEARCH (IT IS APPLICABLE TO SORTED ARRAYS ONLY)

x=input('enter the list')
a=int(input('enter the number to be found'))


n=len(x)

low=0
high=n-1

while low<=high:
    mid=(low+high)/2
    
    if(x[mid]<a):
        low= mid +1
        
    elif (x[mid]>a):
        high= mid-1
        
    else:
        print(x[mid])    