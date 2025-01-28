print("\nData Types.")

x = "Hello World"
print( x , type(x) )
x = 80
print( x , type(x) )
x = 1j
print( x , type(x) )
x = ["apple", "banana", "grapefruit"]
print( x , type(x) )
x = ("pineapple", "kiwi", "orange")
print( x , type(x) )
x = range(9)
print( x , type(x) )
x = {"name" : "Franceva", "age" : 16}
print( x , type(x) )
x = {"banana", "grapefruit", "mango"}
print( x , type(x) )
x = frozenset({"apple", "banana", "cherry"})
print( x , type(x) )
x = False
print( x , type(x) )
x = b"Bye"
print( x , type(x) )
x = bytearray(8)
print( x , type(x) )
x = memoryview(bytes(9))
print( x , type(x) )
x = None
print( x , type(x) )

print("\n\n converting a float to an integer and a string to a float")

y = int(2.5)
print(y)

x = float("500")
print(x, type(x))

#Activity
print("\n\n Activity")
age= input("Enter your age: ")

age= int(age)


year_born = 2025 - age
print("You were born in :" , year_born)



