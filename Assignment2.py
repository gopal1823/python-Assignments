def check_even_or_odd():
    try:
        number = int(input("Please enter a number: "))

        if number % 2 == 0:
            print(f"The number {number} is even.")
        else:
            print(f"The number {number} is odd.")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")


# Call the function
check_even_or_odd()
