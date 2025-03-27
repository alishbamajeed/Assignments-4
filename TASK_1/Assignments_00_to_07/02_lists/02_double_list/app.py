def double_numbers(numbers: list[int]) -> list[int]:
    """
    Takes a list of numbers and returns a new list with each element doubled.
    """
    for i in range(len(numbers)):
        numbers[i] *= 2  
    return numbers


def main():
    """
    CLI-based program to double each number in a list.
    """
    numbers = input("Enter a list of numbers separated by spaces: ")
    numbers = list(map(int, numbers.split()))  
    doubled_numbers = double_numbers(numbers)
    print("Doubled list:", doubled_numbers)


if __name__ == "__main__":
    main()

