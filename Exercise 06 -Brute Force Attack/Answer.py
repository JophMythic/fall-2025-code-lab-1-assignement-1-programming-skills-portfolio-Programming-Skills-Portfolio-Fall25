CORRECT_PASSWORD = "12345"
attempts = 5
print("--- Secure Login System ---")
print(f"You have a maximum of {attempts} attempts to enter the correct password.")
while attempts >= 0:
    user_input = input(f"\Enter password : ")
    if user_input == CORRECT_PASSWORD:
        print("Granting Access")
        break
    if attempts==0:
     print("You have used up the max amount of attempts your account is now locked and the authorities have been informed about account activity")
    else:
        print(f"The password entered is wrong you have {attempts-1} attempts left")
    attempts=attempts-1