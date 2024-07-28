import sys
string = input("Enter a sentence")
words = 1

print(len(string))

for character in string:
    print(len(character))
    sys.exit(0)

for word in string:
    if ' ' in word:
        words = words + 1
        

print(string.upper())
print(string.lower())

print(string)


