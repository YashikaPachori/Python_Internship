print("*****WELCOME TO BMI CALCULATOR*****")
Weight=float(input("Enter your Weight in kg:\n"))
Height=float(input("Enter your Height in m:\n"))
BMI= Weight/(Height)**2

if BMI<18.5:
    print("Underweight")
elif BMI>=18.5 and BMI<25:
    print("Normal")
elif BMI>=25 and BMI<30:
    print("Overweight")
else:
    print("Obesity")
