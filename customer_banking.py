# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

# Constant variables
ACCOUNT_TYPE_SAVINGS = "savings"
ACCOUNT_TYPE_CD = "CD"

def print_account_details(account_type, months, interest_earned, updated_balance):
    """Prints the details of the account type with formatted interest and balance."""
    print(f'Here are the details of your {account_type} account.')
    print(f"For {months} months, you've earned ${interest_earned:,.2f} in interest.")
    print(f"Your {account_type} balance is ${updated_balance:,.2f}")

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """ 
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input(f"Enter your {ACCOUNT_TYPE_SAVINGS} balance: "))
    savings_interest = float(input("Enter your interest rate: "))
    savings_maturity = int(input(f"Enter the {ACCOUNT_TYPE_SAVINGS} duration (months): "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print_account_details(ACCOUNT_TYPE_SAVINGS, savings_maturity, savings_interest_earned, updated_savings_balance)

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input(f"Enter your {ACCOUNT_TYPE_CD} balance: "))
    cd_interest = float(input("Enter your interest rate: "))
    cd_maturity = int(input(f"Enter the {ACCOUNT_TYPE_CD} duration (months): "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print_account_details(ACCOUNT_TYPE_CD, cd_maturity, cd_interest_earned, updated_cd_balance)

if __name__ == "__main__":
    # Call the main function.
    main()
