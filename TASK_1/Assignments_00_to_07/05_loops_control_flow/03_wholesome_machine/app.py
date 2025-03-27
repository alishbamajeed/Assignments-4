def main():
    AFFIRMATION = "I am capable of doing anything I put my mind to."
    
    print("Please type the following affirmation: ")
    print(AFFIRMATION)

    user_feedback = input("> ")  
    
    while user_feedback != AFFIRMATION:  
        print("\nThat was not the affirmation. Try again!")
        print("Please type the following affirmation: ")
        print(AFFIRMATION)
        user_feedback = input("> ")

    print("\nThat's right!")


if __name__ == "__main__":
    main()


