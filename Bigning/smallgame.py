import random

# map each letter to its full name
names = {"s": "Snake", "w": "Water", "g": "Gun"}

# rules: what each item beats
beats = {"s": "w",   # Snake drinks Water
         "w": "g",   # Water rusts Gun
         "g": "s"}   # Gun kills Snake

user = input("Choose (s)nake, (w)ater, or (g)un: ").lower()
comp = random.choice(list(names))

print(f"You chose {names[user]}")
print(f"Computer chose {names[comp]}")

if user == comp:
    print("It's a draw")
elif beats[user] == comp:
    print("You win!")
else:
    print("You lose!")
