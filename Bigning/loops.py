
# # for loop print values from 0 to 9
# for i in range(0,9):
#   # only print even numbers
#   if i % 2 == 0:
#     print("this is a for loop", i)


# # while loop print values from 0 to 9
# i = 0
# while i < 10:
#     # only print even numbers
#     if i % 2 == 0:
#         print("this is a while loop", i)
#     i += 1  # increment i to avoid infinite loop


# for loop print values from 0 to 20 prime numbers
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# for i in range(0, 21):
#     if is_prime(i):
#         print("this is a for loop", i)


# for loop prective 
# val = "*"

# for i in range(5,1,-1):
#   print(val*i)



# 4,5,6,7,8,9,10
# 8,10,12,14,16,18,20
# 12,15,18,21,24,27,30
# 16,20,24,28,32,36,40
# for loop print values from 4 to 10, increment by 2  


# for val in range(1,5):
#   row = [str(val*i) for i in range (4,11)]
#   print(" ".join(row))



# while loop print values from 0 to 9
password = 'shahmir'
attempt = 1

while attempt <= 3:
    input_password = input("Enter your password: ")
    if input_password == password:
        print("Password is correct")
        break  # Exit the loop after correct password
    elif attempt == 3:
        print("You have entered the wrong password 3 times")
        break
    else:
        attempt += 1  # Fixed typo here
        print("Password is incorrect")
 