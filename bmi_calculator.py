weight=float(input("Enter your weight in kilograms\n"))
height=float(input("Enter your height in meters\n"))

BMI = weight/(height*height)
print(BMI)
if BMI <18.5: 
   print("underweight") 
elif BMI >25:
   print("overweight")
elif BMI >18.5 and BMI <25:
   print("Normal")