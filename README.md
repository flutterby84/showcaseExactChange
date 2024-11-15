Step 1: Open the Project
Use a Python editor like VSCode, PyCharm, or a text editor of your choice.
Make sure you are inside the project folder (showcase-exact-change).

Step 2: Run the Program
In the terminal, run:
bash
Copy code
python calculate_change.py
The program will ask you to enter an amount of money:
java
Copy code


Step 3: Enter an Amount
Type in a dollar amount and press Enter.(Enter an amount (Ex, 19.99):)

Step 4: View the Results
The program will display the breakdown of bills and coins needed for the total amount:
(Ex. '19.99')
1 - $10 bill(s)
1 - $5 bill(s)
4 - $1 bill(s)
3 - quarter(s)
2 - dime(s)
0 - nickel(s)
4 - penny(s)


--How the program works: 




The program starts by asking the user to enter an amount of money, such as `19.99`. To ensure the input is valid, it uses built-in input validation. This checks that the user enters a numeric value (like `19.99`) and not invalid data, such as letters or symbols. If the input is invalid, the program prompts the user again until a correct value is entered.

Once a valid amount is provided, the program converts it into cents (e.g., `19.99` becomes `1999` cents). Working with cents ensures precise calculations without rounding errors often associated with floating-point numbers. After that, the program defines the available US currency denominations, including $10, $5, $1 bills, and coins like quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢).

The program calculates the change using these denominations, starting with the largest and working its way down to the smallest. It determines how many of each denomination are needed and ensures the total reaches zero cents. The results are then displayed, showing the breakdown of bills and coins required for the given amount.