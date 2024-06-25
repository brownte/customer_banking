# Module 3 Challenge - Customer Banking Project

This project simulates a customer banking system where users can interactively create and manage savings and CD (Certificate of Deposit) accounts. The program calculates interest earned based on user input for account balances, interest rates, and durations in months.

## Files and Structure

### `customer_banking.py`

This is the main script that interacts with the user and orchestrates the creation and management of savings and CD accounts.

#### Functions:
- **`print_account_details(account_type, months, interest_earned, updated_balance)`**: 
  Prints detailed account information including account type, interest earned over a specified period, and updated balance.

- **`main()`**: 
  - Prompts the user to input savings account details (balance, interest rate, months).
  - Calls `create_savings_account()` to create the savings account and calculate interest.
  - Prints the details of the savings account.
  - Prompts the user to input CD account details (balance, interest rate, months).
  - Calls `create_cd_account()` to create the CD account and calculate interest.
  - Prints the details of the CD account.

### `cd_account.py`

Handles CD account functionalities including creation, interest calculation, and balance updating.

#### Functions:
- **`create_cd_account(balance, interest_rate, months)`**: 
  - Creates an instance of `Account` for CD.
  - Calculates interest based on provided parameters.
  - Updates CD account balance and interest.
  - Returns updated balance and interest earned.

### `savings_account.py`

Handles savings account functionalities including creation, interest calculation, and balance updating.

#### Functions:
- **`create_savings_account(balance, interest_rate, months)`**: 
  - Creates an instance of `Account` for savings.
  - Calculates interest based on provided parameters.
  - Updates savings account balance and interest.
  - Returns updated balance and interest earned.

### `Account.py`

Defines the `Account` class which encapsulates the basic functionality of any account.

#### Class: `Account`
- **Attributes**: 
  - `balance`: Represents the account balance.
  - `interest`: Represents the APR interest rate.

#### Methods:
- **`__init__(balance, interest)`**: 
  - Initializes an account instance with provided balance and interest rate.

- **`set_balance(balance)`**: 
  - Sets a new balance for the account.

- **`set_interest(interest)`**: 
  - Sets a new interest rate for the account.

- **`get_balance()`**: 
  - Returns the current balance of the account.

- **`get_interest()`**: 
  - Returns the current interest rate of the account.

- **`calculate_interest(months)`**: 
  - Calculates the interest earned over a specified number of months based on the current balance and interest rate.

## Usage

1. **Run `customer_banking.py`**: 
   - Execute this script to interact with the banking system.
   - Follow the prompts to enter details for savings and CD accounts.
   - The program will calculate and display interest earned and updated balances for each account.