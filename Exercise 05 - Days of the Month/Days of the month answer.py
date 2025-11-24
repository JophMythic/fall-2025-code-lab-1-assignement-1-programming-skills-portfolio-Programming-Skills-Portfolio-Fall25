month_days = {
    1: 31, 
    2: 28,  
    3: 31,  
    4: 30,  
    5: 31,  
    6: 30,  
    7: 31,  
    8: 31,  
    9: 30,  
    10: 31, 
    11: 30, 
    12: 31  
}
print("Month Day Counter")
try:
    month_number_str = input("Enter the month number (1-12): ").strip()
    month_number = int(month_number_str)
except ValueError:
    print("Error: Invalid input. Please enter a whole number.")
    exit()
if month_number < 1 or month_number > 12:
    print("Invalid month number. Please enter a number between 1 and 12.")
else:
    days = month_days[month_number]
    if month_number == 2:
        is_leap_input = input("Is the year a leap year? (y/n): ").strip().lower()
        if is_leap_input == 'y':
            days = 29
            print(f"Month {month_number} has {days} days (Leap Year).")
        else:
            print(f"Month {month_number} has {days} days.")
    else:
        print(f"Month {month_number} has {days} days.")
