"""Imports the SavingsAccount class and attributes from the Account.py file."""

from Account import SavingsAccount

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    
    savings_account = SavingsAccount(balance, interest = 1.25)

    # Calculate interest earned
    
    monthly_interest_rate = interest_rate / 12 /100
    interest_earned_savings = balance * (monthly_interest_rate) * months

    # Update the savings account balance by adding the interest earned
   
    new_savings_balance = balance + interest_earned_savings

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    
    savings_account.set_balance(new_savings_balance)

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    
    savings_account.set_interest(interest_earned_savings)

    # Return the updated balance and interest earned.
     
    return new_savings_balance, interest_earned_savings

# Testing code

# starting_balance = float(500.00)
# interest_rate = float(1.25)
# months = int(12)

# new_savings_balance, interest_earned_savings = create_savings_account(starting_balance, interest_rate, months )

# print(starting_balance, interest_earned_savings, new_savings_balance)