# Get current age of user
age = int(input("How old are you?\n"))
# Get the age the user would like to live
like_to_live = int(input("How many years do you want to live?\n"))
# Calculate the elapsed life
days_elapsed = age * 365
weeks_elapsed = age * 52
months_elapsed = age * 12
# Calculation of remaining life
yesrs_remaining = like_to_live - age
days_remaining = yesrs_remaining * 365
weeks_remaining = yesrs_remaining * 52
month_remaining = yesrs_remaining * 12
# Print result
print(f"{days_elapsed} days, {weeks_elapsed} weeks and {months_elapsed} months have passed since your life")
print(f"You have {days_remaining} days, {weeks_remaining} weeks and {month_remaining} months left to live")