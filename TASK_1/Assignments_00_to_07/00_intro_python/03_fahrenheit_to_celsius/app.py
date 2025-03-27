def main():

    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    

    print(f"Temperature: {fahrenheit:.1f}°F = {celsius:.1f}°C")

if __name__ == '__main__':
    main()
