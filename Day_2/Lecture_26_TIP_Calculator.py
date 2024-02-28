print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10,12 0r 15? "))
people = int(input("How many people to split the bill? "))

# 1st method:

# tip_as_percentage = tip / 100
# total_tip_amount = bill * tip_as_percentage
# total_bill = bill + total_tip_amount
# final_splited_amount = total_bill / people

# 2nd method:
total_bill = bill * (1+ tip /100)
final_splited_amount = total_bill / people


print(f"Each person shout pay:  ${final_splited_amount}")
#O/P: Each person shout pay:  $0.47008547008547014

print("Each person shout pay: $",format(final_splited_amount,".2f"))
# O/P: Each person shout pay:  $0.47