year = int(input("Enter the year: "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(f"the year {year} is  LEAP year")
    else:
      print(f"the year {year} is NOT LEAP year")

  else:
    print(f"the year {year} is LEAP year")

else:
  print(f"the year {year} is NOT LEAP year")
