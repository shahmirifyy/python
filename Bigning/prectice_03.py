values = []
sum=0
print("Enter the names of 3 Value for sum:")

for i in range(3):
    number = int(input(f"Enter number {i + 1}: "))
    values.append(number)
    sum=(sum + number)

print("\nYou entered these number:")
print(values)
print("\nFollowing is the sum of these numbers:")
print(sum)
