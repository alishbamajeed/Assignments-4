def main():
    print("Welcome to the Number Addition Program!")
    try:
        num1 = int(input("Please enter your first number: "))
        num2 = int(input("Please enter your second number: "))
        total = num1 + num2
        print(f"The sum of {num1} and {num2} is: {total}")
    except ValueError:
        print("Error: Please enter valid numbers only.")

if __name__ == '__main__':
    main()



