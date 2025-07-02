 
    
# Generate table
def generate_table(n):
    for i in range(1, 11):
       #  The yield keyword in Python is used inside a function to make it a generator. Instead of returning a single value and ending the function (like return), yield pauses the function and returns a value, but the function's state is saved so it can resume from where it left off the next time it's called.
        yield f"{n} x {i} = {n * i}"

# Loop from 1 to 10
for i in range(2, 11):
    print(f"\nMultiplication Table for {i}:")
    with open(f"File/Tables/table_{i}.txt", "w") as file:
        # Write each line of the table to a file
        for line in generate_table(i):
            file.write(line + "\n")
        
