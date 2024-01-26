name= input("Enter your name\n")
age= input("Enter your age\n")
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

f = open("bmi_calculator.csv", "a+")
f2 = open("bmi_calculator.csv", "r+")

file_content = f2.read()

headings = "Name,Age,Weight,Height,BMI\n"
if headings not in file_content:
   f.write(headings)

f.write(f"{name},{age},{weight},{height},{BMI}\n")
f.close()
f2.close()
