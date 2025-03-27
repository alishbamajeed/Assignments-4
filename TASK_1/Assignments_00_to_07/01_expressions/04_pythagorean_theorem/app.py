import math  

def main():
    """ Command-line version of the Pythagorean Theorem Calculator """
    try:
        ab = float(input("Enter the length of AB: "))  
        ac = float(input("Enter the length of AC: "))  
        bc = math.sqrt(ab**2 + ac**2)  
        print(f"The length of BC (the hypotenuse) is: {bc}")
    except ValueError:
        print("Please enter a valid number.")


if __name__ == '__main__':
    main()

