lower = int(input("enter a lower range: "))
upper = int(input("enter a upper range: "))

print("Prime number between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    print("current number is", num)
    if num > 1:
        for i in range(2, num):
            print("current divisor is", i)
            if(num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print("current prime number is", num)
    print("-----------------------------")