hieght = float(input("Pls enter your height: "))
weight = float(input("Pls enter your weight: "))

BMI = weight / (hieght * 100)**2
print("BMI is ", BMI)

if BMI <= 18.4:
    print("You are underweight")
elif BMI <= 24.9:
    print("You are healthy")
elif BMI <= 29.9:
    print("You are overweight ")
elif BMI <= 34.9:
    print("You are severely overweight")
elif BMI <= 39.9:
    print("Tou are obese")
else:
    print("You are severely obese ")