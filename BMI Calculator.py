print("Welcome to the BMI Analyzer!")
print(" ")

name = input("What is your name?")
lb_weight = int(input("What is your weight in pounds?"))
in_height = int(input("What is your height in inches?"))

print(" ")

bmi = (lb_weight * int(703)) / (in_height ** 2)

print(name)
print("BMI:")
print(bmi)

if bmi < 18:
    print("You are underweight.")

elif int(bmi) in range(18, 26):
    print("You have a normal weight.")

elif int(bmi) in range(26, 31):
    print("You are overweight.")

elif bmi in range(30, 36):
    print("You fall under the obesity class: 1.")

elif bmi in range(35, 41):
    print("You fall under the obesity class: 2")

elif bmi >= 40:
    print("You fall under the obesity class: 3")

print(" ")

input("Thanks for Testing!")
