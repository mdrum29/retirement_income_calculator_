from src.persona_data import User
from src.monte_carlo_simulations import get_portfolio_returns
from src.calculate_portfolio_balance import calculate_accumulation_period, optimizer

def RIC(currentAge, retirementAge, horizonAge, riskTolerance, startingBalance, savings, target_successRate):   
    user1 = User(currentAge, retirementAge, horizonAge, riskTolerance, startingBalance, yearlySavings, target_successRate)
    portfolio_returns = get_portfolio_returns(user1)
    _, accumulation_array = calculate_accumulation_period(user1, portfolio_returns)
    optimizer(user1, portfolio_returns, accumulation_array)

if __name__ == '__main__':
# Get user input for the variables
    currentAge = int(input("Enter your current age: "))
    retirementAge = int(input("Enter your retirement age: "))
    horizonAge = int(input("Enter your horizon age: "))
    riskTolerance = float(input("Enter your risk tolerance (1-5, 1 is the lowest. 5 is the highest.): "))
    startingBalance = float(input("Enter your starting balance: "))
    yearlySavings = float(input("Enter your expected monthly savings: "))*12
    target_successRate = float(input("Enter your target success rate as a decimal: "))

    RIC(currentAge, retirementAge, horizonAge, riskTolerance, startingBalance, yearlySavings, target_successRate)
