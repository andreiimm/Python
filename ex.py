def is_valid_age(age):
    if 18 <= age <= 65:
        return True 
        
    else:
        return False  

age = float(input("Please enter an age: "))   
print(is_valid_age(age))  
