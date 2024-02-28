# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = int(weight) / float(height)**2

if BMI<= 8.5:
  print("you Body Mass Index is ",format(BMI,".2f"),", you are underweight")
elif BMI <25:
  print("you Body Mass Index is ",format(BMI,".2f"),", you are normslweight")
elif BMI <30:
  print("you Body Mass Index is ",format(BMI,".2f"),", you are slightly overweight")
elif BMI <35:
  print("you Body Mass Index is ",format(BMI,".2f"),"BMI}, you are obese")
else:
  print("You are clinically obese")
    


