#loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter
fruit = input("Wot fruit? ")
index = len(fruit) - 1
while index > -1:
    letter = fruit[index]
    print(letter)
    index = index - 1
print("done")
