n = int(input("Enter the value: "))

# if(n < 0):
#     print(f"{n} is a negative number ")
# elif(n == 0):
#     print(f"{n} is zero ")
# elif(n > 0):
#     print("The number is greater than zero ")
# elif(n != 0):
#     print("The number is not equal to zero ")

# elif(n <= 0):
#     print("The number is lexx than or equal to zero")
# else:
#     print("The number is greater or equal to zero")

if(n < 0):
    print("The number is negative")
elif(n > 0):
    if (n >= 0 and n <= 10):
        print("Number is between 1 and 10")
    elif (n > 10 and n <= 15):
        print("Number is between 10 and 15 ")
    elif (n > 15 and n <= 20):
        print("Number is between 15 and 20 ")
    else:
        print("Number is greater than 20 ")
else:
    print("Number is zero")
