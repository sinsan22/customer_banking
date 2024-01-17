customer_banking

The Customer Banking is a budget tool for Python. It asks customers for
inputs for a CD account and a savings account and then calculates the
updated balances based on interest rates and maturity lengths. The
project takes customer inputs for initial balances, interest rates, and
account maturation.

Customer Banking

The Customer Banking module requires the create_cd_account and the
create_savings_account functions. Both the create_cd_account and
create_savings_account requires classes imported from the account.py
file. No outside modules are required. Account.py File

This file creates the Account and SavingsAccount Classes. The original
file only contained the Account Class, but the instructions in the
create_saving_account file called for a SavingsAccount Class, so I
created one for practice. The \_ \_init\_ \_ method is called during the
creation of each class. It takes the balance and interest parameters and
initializes the self.balance and self.interest variables with the
provided values. Each class includes the set_balance and the
set_interest methods. The set_balance method sets the initial balance
using the balance parameter. The set_interest method sets the interest
earned for each account. The self.balance and the self.interest
variables allow for updates based on customer inputs.

create_cd_account File

The create_cd_account file uses the Account Class created in the
account.py file. It creates a CD account, initializes the balance,
calculates earned interest, and updates the balance. It takes inputs for
balance, interest rate, and the months to maturity. It returns the
interest earned and the updated balance. Note: there is code commented
out at the bottom of the file. Use this to test the code and formulas
before progressing to the next piece of the project.

create_savings_account File

The create_savings_account file uses the SavingsAccount Class created in
the account.py file. It creates a savings account, initializes the
balance, calculates earned interest, and updates the balance. It takes
inputs for balance, interest rate, and the months to maturity. It
returns the interest earned and the updated balance. Note: there is code
commented out at the bottom of the file. Use this to test the code and
formulas before progressing to the next piece of the project.

customer_banking File

This is the front-facing piece of the project. It uses a function that
takes customer inputs for initial balances, interest rates, and months
to maturity and applies the imported create_cd_account and
create_savings_acount functions. The end result is a formatted output
that gives the initial balance, the interest earned, and the updated
balance for the the CD and savings accounts.
