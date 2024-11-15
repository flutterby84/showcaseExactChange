def get_valid_input():
    while True:
        user_input = input("Enter an amount (e.g., 19.99): ")
        try:
            # Trys to convert the input to a float
            amount = float(user_input)
            if amount < 0:
                print("Please enter a positive number.")
            else:
                return amount
        except ValueError:
            # Handle cases where the input is not a valid number
            print("Invalid input. Please enter a valid number (Ex., 19.99).")
def calculate_change(amount):
    """
    Calculates the exact change in bills and coins.
    """
    # Convert the dollar amount to cents
    cents = int(round(float(amount) * 100))

    # Define the denominations in  the value of cents
    denominations = [1000, 500, 100, 25, 10, 5, 1]  # $10, $5, $1, quarters, dimes, pennies
    counts = [0] * len(denominations)  # To store the count of each denomination

    # Calculate the change (program loops over the denominations list, using the index of 1
    # to access both the value of the denomination (denominations{i}) and the corresponding
    # count in counts list (counts[i}) this ensures calc is performed sequentially
    for i in range(len(denominations)):
        while cents >= denominations[i]: #checks for remainder to see if >= current denomination
            cents -= denominations[i] #if true deducts from total cents and keeps doing so until cant then moves forward in list
            counts[i] += 1  #adds count to that denomination

    # Print the result
    print(f"{counts[0]} - $10 bill(s)")
    print(f"{counts[1]} - $5 bill(s)")
    print(f"{counts[2]} - $1 bill(s)")
    print(f"{counts[3]} - quarter(s)")
    print(f"{counts[4]} - dime(s)")
    print(f"{counts[5]} - nickel(s)")
    print(f"{counts[6]} - penny(s)")

# Ask the user to input an amount
if __name__ == "__main__":
    amount = input("Enter an amount (Ex., 19.99): ")
    calculate_change(float(amount))
