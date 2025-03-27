INCHES_IN_FOOT: int = 12  
def main():
    """ Command-line version of Feet to Inches Converter """
    try:
        feet = float(input("Enter number of feet: "))  
        inches = feet * INCHES_IN_FOOT  
        print(f"That is {inches} inches!")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == '__main__':
    main()


