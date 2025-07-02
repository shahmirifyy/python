def avg():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=int(input("Enter third number: "))
    average = (a + b + c) / 3
    print("The average is:", average)
  
# avg()
# # fucntion avg is defined to take three arguments
# def avg(a,b,c):
#     average = (a + b + c) / 3
#     return average

# av= avg(10,5,5) 
# print("The average is:", av)


# fucntion avg is defined to with default arguments
# def avg(a=0,b=0,c=0):
#     average = (a + b + c) / 3
#     return average

# av= avg() 
# print("The average is:", av)


# fucntion fectorial is defined to take three arguments
def fectorial(n=0):
  if n==1 or n==0:
    return 1
  return n * fectorial(n-1)


av= fectorial(4) 
print("The average is:", av)  