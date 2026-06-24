n = int(input("Enter how many rows you want for your pyramid: "))

for i in range(n):
    for i in range(i+1):
        print("*" , end="")
    print()
    