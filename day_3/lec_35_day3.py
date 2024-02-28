print("Welcome to Python Pizza Deliveries ")
bill = 0
wants_pizza = input("Do you want to eat pizza? Y or N :")
if wants_pizza == 'y' or 'Y':

  size_of_pizza = input(" What size pizza do you want? S,M or L :")

  if size_of_pizza == 'S' or 's':
    bill = 15

  if size_of_pizza == 'M' or 'm':
    bill = 20

  if size_of_pizza == 'L' or 'l':
    bill = 25

  want_pepperoni = input("Do you want pepperoni? Y/N :")
  if want_pepperoni == "Y" or 'y':
    if size_of_pizza == 'S' or 's':
      bill += 2
    elif size_of_pizza == 'M' or 'L' or 'm' or 'l':
      bill += 3

  wants_extra_cheese = input("Do you want extra cheese? Y or N :")
  if wants_extra_cheese == 'Y' or 'y':
    bill += 1

  print(f"Total Bill is{bill}")

elif wants_pizza == 'N' or 'n':
  print("Thanks for  comming, see you soon.")
