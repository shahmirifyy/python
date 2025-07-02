import random

def game():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  secret_number = random.randint(1, 100)
  return secret_number

value= game()
number=0
with open("File/guessing_game.txt") as f:
      content = f.read()
      print("Last number in the file: ", content)
      print("new number in the file: ", value)
      if(content == "" ):
        number= value
      else:
        number=int(content)
        
print(f"The secret {number} is saved in the file.",number ,value, number >= value)
if(number <= value):
 with open("File/guessing_game.txt",'w') as f:
         
    f.write(str(value))
else:  
        print("The Number is less then prevoius!")    
    