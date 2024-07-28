Name = "AbuTalha"

"""This will print first four character"""
print(Name[0:4])    


# Zero will be assign by python auto
print(Name[:4])

# It will print from N and ends with zero

print(Name[2:5])

# It will print the whole array
print(Name[:])



# Negative Slicing

print(Name[:-4])
print(Name[:len(Name)-4])

for i in Name:
    print(i, end="")