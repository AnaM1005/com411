#Body Mass Index 
print("What is your name human?")
name = input()

print("How old are you?(in years)")
age = int(input())

print("How tall are you?(in metres)")
height = float(input())

print("How much do you weight? (in kilograms)")
weight = float(input())

bmi = weight / (height ** 2)

print(str(name), "your age is", int(age), "and your BMI is {:.2f}.".format (bmi))
