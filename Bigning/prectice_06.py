# # to find the greatest number from user input
# numbers= set()

# for i in range(4):
#   numbers.add(int(input(f"Enter number {i+1}: ")))
  
# print("The greatest numbers is:", max(numbers))



# to find the greatest number from user input another way
# numbers= set()

# for i in range(3):  
#   number=int(input(f"Enter number {i+1}: "))
#   if len(numbers) ==0:
#     print("i am adding number because there is no value in the set.")
#     numbers.add(number)
#   elif number > max(numbers):
#     print("This number is not greater than the current greatest number.")
#     numbers.clear()
#     numbers.add(number)

# print("greatest number",numbers)

# user passed or fail in the exams


# users = {}
# for i in range(1):
#     total_marks = int(input("Enter total marks: "))
#     name = input("Enter your name: ")
#     obtained_marks = int(input(f"Enter your marks for {name}: "))
    
#     percentage = (obtained_marks / total_marks) * 100
#     status = "pass" if percentage >= 33 else "fail"
    
#     # Store student data in a nested dictionary
#     users[name] = {
#         "marks": obtained_marks,
#         "percentage": round(percentage, 2),
#         "status": status
#     }
  
# print(users)


# A spam comment is defiend as a text containing following keywords:
# "Make a lot of money",, "Buy now", "subscribe this", "click this"

# spam_keywords = [
#     "make a lot of money",
#     "buy now",
#     "subscribe this",
#     "click this"
# ]

# text = input("Enter your text: ")
# lower_text = text.lower()

# #1st way Check if any spam keyword is contained in the text
# # if any(keyword.lower() in lower_text for keyword in spam_keywords):
# #     print("⚠️ Spam word detected!")
# # else:
# #     print("✅ No spam words found.")

# #2nd way Check if any spam keyword is contained in the text
# for keyword in spam_keywords:
#     if keyword.lower() in lower_text:
#         print(f"⚠️ Spam word detected: {keyword}")
#         break
# else:
#     print("✅ No spam words found.")


