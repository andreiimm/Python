print("Welcome to the Personalised User Profile Generator!\nThis program collects and processes user information.") #the purpose of this is to greet the user when running the program

name= input("\nEnter your full name:")
age= int(input("Enter your age:"))
height=float(input("Enter your height:"))
fvrt_prg_lng= input("Enter your favourite programming language:")
fvrt_nmb= int(input("Please enter your favourite Number:"))
descr= input("Please enter a short description about yourself:")
#converting
age = float(age)
height= int(height)
fvrt_nmb= str(fvrt_nmb)

# slicing
first_name= name.split()[0]
print(f"Hello, {first_name}! ")