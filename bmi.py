print("BMI CALCULATOR")
w = float(input("Enter the weight in KG: "))
h = float(input("Enter the height in CM: "))
hh = (h / 100) ** 2
bm = (w / hh)
bmi = round(bm, 2)
print('Your BMI is: ', bmi)

if bmi < 18.5:
    print("You are Underweight")
elif bmi <= 24.9:
    print("Your weight is Normal")
elif bmi <= 29.9:
    print("You are Overweight")
else:
    print("You are very Overweight")
