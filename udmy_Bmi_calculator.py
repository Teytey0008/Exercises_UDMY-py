

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))


bmi = weight / (height ** 2)

if bmi <= 18.5:
    bmi_category = "UNDERWEIGHT"
elif bmi <= 25:
    bmi_category = "NORMAL WEIGHT"
elif bmi <= 30:
    bmi_category = "SLIGHT OVERWEIGHT"
elif bmi <= 35:
    bmi_category = "OBESE"
else:
    bmi_category = "CLINICALLY OBESE"

print("Your BMI is {:.1f}, and you are {}".format(bmi, bmi_category))    