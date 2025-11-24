def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

def main():
    number = int(input("Enter a number to check: "))
    
    result = even_or_odd(number)
    
    print(f"The number {number} is {result}.")

if __name__ == "__main__":
    main()