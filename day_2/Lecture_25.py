# Assume that your total Age is 90 years, then take input as age and  calculate remaining months,weeks & days.  

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
int_age = 90 - int(age)
months = int_age * 12
weeks = int_age * 52
days = int_age * 365

msg = f"You have {days} days, {weeks} weeks, and {months} months left."
print(msg)