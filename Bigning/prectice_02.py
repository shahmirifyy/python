user = []

print("Enter the names of 5 fruits:")

for i in range(5):
    name = input(f"Enter name {i + 1}: ")
    marks = input(f"Enter Marks {i + 1}: ")
    user.append({marks,name})

print("\nYou entered these name and marks:")
print(user)
