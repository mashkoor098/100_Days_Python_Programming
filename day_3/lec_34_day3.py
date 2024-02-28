print("Hi, wellcome to the rolercoster")

height = int(input("what is your height in cm:  "))
bill = 0
if height >= 120:
  age = int(input("what is your age"))
  if age <= 12:
    bill = 5
    print("you have to pay $5")

  if age < 18:
    bill = 7
    print("you have to pay $7")

  if age >= 18:
    bill = 12
    print("you have to pay $12")

  photo = input("Do you want to take photo? y/n : ")
  if photo == 'y':
    bill += 3
    print(f"Your total bill is {bill}")
  else:
    print(f"Your total bill is {bill}")

else:
  print("You can't ride")
