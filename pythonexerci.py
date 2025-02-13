# Exercise 1
# \t is used for adding indentation in the output code (space)
print("1.Poem Exercise:")
print("\nTwinkle, twinkle,little star,")
print("\tHow I wonder how you are!")
print("\t\tUp above the world so high,")
print("\t\tLike a diamon in the sky.")
print("Twinkle, twinkle,little star,")
print("\tHow I wonder how you are!")

# Exercise 2
print("\n\n\n2.Area of circle calculation:")

r = float(input("r ="))

Area = 3.14 * r**2

print("Area =" , Area)

# Exercise 3
# the f-string allows the program to take what is in curly brackets {} , make it a string and then int transforms it back to an integer
print("\n3.Number expansion calculator:")

n = int(input("n ="))

result = n + int(f"{n}{n}") + int(f"{n}{n}{n}")

print("Result :", result)