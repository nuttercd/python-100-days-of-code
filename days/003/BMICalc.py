weight = float(input("Welcome to the BMI Calculator. Please enter your weight in kg: "))
height = float(input("Enter in your height in m: "))

BMI = round(weight / height**2, 1)
if(BMI < 18.5):
    print(f"Your BMI is {BMI} and you are underweight")
elif (BMI > 18.5 and BMI < 25):
    print(f"Your BMI is {BMI} and have a normal weight")
elif (BMI > 25 and BMI < 30):
    print(f"Your BMI is {BMI} and you are overweight")
elif (BMI > 30 and BMI < 35):
    print(f"Your BMI is {BMI} and you are obese")
elif (BMI > 30):
    print(f"Your BMI is {BMI} you are clinically obese")

