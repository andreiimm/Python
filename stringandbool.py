print(" 1. ")
x = "I like to eat" 
print( x.upper())
print(x.replace("like" , "hate"))
print(x.split(" "))

print("\n 2.")
x= float(input("Enter a number: "))
y= float(input("Enter a second number:"))
if x>y:
    print("First number is greater")
elif x<y:
    print("First number is less than the second number")
else:
    print("Numbers are equal")

print("\n 3.")

z = float(input("Enter a number:"))
if z >=10 and z<=20:
          print("The number is between 10 and 20")
else :
    print("The number is NOT between 10 and 20")

print("\n\n\n Homework!")

sent= input("Please Type a sentence... : ")

vowels = "AEIOUaeiou"

vowel_count = sum(sent.count(v) for v   in vowels)

print("The number of vowels is :", vowel_count)

print("\n\n 2.Number checking")

num=float(input("Enter a number: "))
if num>0:
    print("number is positive")
elif num<0:
    print("number is negative")
else:
    print('Number is zero')

