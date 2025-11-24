names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
search_term = input("Enter the name to search for: ")

if search_term in names:
    print(f"'{search_term}' was found in the list.")
else:
    print(f"'{search_term}' was not found in the list.")