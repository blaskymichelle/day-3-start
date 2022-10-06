print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120: 
  print("You can ride the rollercoater!")
else:
  print("Sorry, you have to grow taller before you can ride.")


bmi=18
bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f" Your bmi is {bmi}, you have a normal weight.")    
elif bmi < 30:
    print(f" Your bmi is {bmi}, you are overweight.")    
elif bmi < 35:
    print(f" Your bmi is {bmi}, you are obese.")  
else:
    print(f" Your bmi is {bmi}, you are clinically obese.")       