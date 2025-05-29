pattern = int(input("Enter the size of the pattern: "))
row = 0
while row < pattern:
 for i in range(pattern):
    for j in range(pattern):
            print("*", end="")
    print() 
    row += 1

# This code will print a square pattern of asterisks based on the input size.
