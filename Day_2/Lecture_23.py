# Calculate the Body Mass Index (BMI) using Hight & wieght

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = int(weight) / float(height)**2

#The BMI value is in float type to concatinate with string we have to convert in into string type 
BMI_as_string = str(int(BMI))

print("Your Body Mass Index is:  "+BMI_as_string)

