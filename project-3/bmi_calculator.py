# Get height & weight
height = float(input("Please enter your height in m:\n"))
weight = float(input("Please enter your weight in kg:\n"))
# Calculate bmi
bmi = round(weight / height ** 2)
# Print result
if bmi < 18.5:
    print(f"Your bmi is {bmi}, and you are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, and you have a normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, and you are over weight.")    
elif bmi <35:
    print(f"Your bmi is {bmi}, and you are obese.")
else:
    print(f"Your bmi is {bmi}, and you are clinically obese.")        