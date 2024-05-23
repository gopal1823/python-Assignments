def main():

    try:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))

        if length > 0 and width > 0:
            area = length * width
            print(f"The area of the rectangle is: {area}")
        else:
            # Handle the case where either length or width is not positive
            print("Error: Both length and width must be positive numbers.")

    except ValueError:
        print("Error: Please enter valid numbers for length and width.")


if __name__ == "__main__":
    main()
