number = float(input("Enter your marks "))

# match number:
#     case > 90 and < 100 :
#         print("You got A+ grade")

if (number >= 90 and number < 100):
    print("you got A+ grade ")
elif (number >=  80 and number < 90 ):
    print("You got A grade ")
elif (number >= 70 and number < 80):
    print("You got B grade ")
elif (number >= 60 and number < 70):
    print("You Got C grade ")
elif (number >= 50 and number < 60):
    print("You Got D Grade ")
elif (number < 50):
    print ("You are Fail ")
else:
    print("Invalid Score Score Must be less than 100")