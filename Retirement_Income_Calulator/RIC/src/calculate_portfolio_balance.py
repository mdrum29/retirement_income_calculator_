from portfolio_allocations import getAllocation
from persona_data import User
from monte_carlo_simulations import get_portfolio_returns
import numpy as np
np.set_printoptions(precision=2)

# currentAge = 27
# retirementAge = 60
# horizonAge = 100
# riskTolerance = "VERY_AGGRESSIVE"
# startingBalance = 70000
# yearlySavings = 20000
# target_SR = .85

# user1 = User(currentAge, retirementAge, horizonAge, riskTolerance, startingBalance, yearlySavings, target_SR)
# portfolio_returns = get_portfolio_returns(user1)

def calculate_accumulation_period(USER, portfolio_returns):

    # calculate portfolio balances through retirement
    portfolioBals = [USER.startingBalance] * portfolio_returns.shape[0]
    for yr in range(USER.accumulationYears):

        if yr == 0:
            EOY_bal = portfolioBals[yr] * (1 + portfolio_returns[:,yr]) + USER.yearlySavings 
        else:
            EOY_bal = portfolioBals[:, yr] * (1 + portfolio_returns[:,yr]) + USER.yearlySavings 

        portfolioBals = np.column_stack((portfolioBals,EOY_bal))


    retirement_p25 = np.percentile(portfolioBals[:,-1],25)
    retirement_p50 = np.percentile(portfolioBals[:,-1],50)
    retirement_p75 = np.percentile(portfolioBals[:,-1],75)

    accumulation_results = {"median_balance": retirement_p50, "25percentile": retirement_p25, "75percentile": retirement_p75}

    print("")
    print("Projected Retirement Balances ||  Most likely:", '$ {:0,.2f}'.format(retirement_p50) , "|  Worst_case: ", '$ {:0,.2f}'.format(retirement_p25), " |  Best_case: ", '$ {:0,.2f}'.format(retirement_p75))
    accumulation_array = portfolioBals
    return accumulation_results, accumulation_array

# accum_res, accumulation_array = calculate_accumulation_period(user1, portfolio_returns)

def calculate_income_period(USER, portfolio_returns, accumulation_array, sustainable_withdrawal):

    # calculate portfolio balances through retirement
    portfolioBals = accumulation_array[:, -1]
    portfolio_returns = portfolio_returns[:,USER.accumulationYears:]

    for yr in range(USER.incomeYears):
        
        if yr == 0:
            EOY_bal = (portfolioBals[:] - sustainable_withdrawal) * (1 + portfolio_returns[:,yr])
            # EOY_bal = np.clip(EOY_bal,0,None)
        else:
            EOY_bal = (portfolioBals[:, yr] - sustainable_withdrawal) * (1 + portfolio_returns[:,yr]) 
            # EOY_bal = np.clip(EOY_bal,0,None)

        portfolioBals = np.column_stack((portfolioBals,EOY_bal))
    final_balances = portfolioBals
    isZero = final_balances[:,USER.incomeYears] <= 0
    successRate = 1-sum(isZero)/1000 # number of zero balance in final year over number of paths

    p25 = np.percentile(final_balances[:,-1], 25)
    p50 = np.percentile(final_balances[:,-1], 50)
    p75 = np.percentile(final_balances[:,-1], 75)

    return successRate, (p25, p50, p75)

# successRate = calculate_income_period(user1, portfolio_returns, accumulation_array, 206200)

def optimizer(USER, portfolio_returns, accumulation_array):
    successRate = 1
    optimal_withdrawal = 0

    while successRate > USER.target_successRate:
        successRate, p = calculate_income_period(USER, portfolio_returns, accumulation_array, optimal_withdrawal)

        optimal_withdrawal += 100000

    while successRate < USER.target_successRate:
        successRate, p = calculate_income_period(USER, portfolio_returns, accumulation_array, optimal_withdrawal)

        optimal_withdrawal -= 10000

    while successRate > USER.target_successRate:
        successRate, p = calculate_income_period(USER, portfolio_returns, accumulation_array, optimal_withdrawal)

        optimal_withdrawal += 1000

    while successRate < USER.target_successRate:
        successRate, p = calculate_income_period(USER, portfolio_returns, accumulation_array, optimal_withdrawal)

        optimal_withdrawal -= 100

    while successRate > USER.target_successRate:
        successRate, p = calculate_income_period(USER, portfolio_returns, accumulation_array, optimal_withdrawal)

        optimal_withdrawal += 10

    while successRate < USER.target_successRate:
        successRate, p = calculate_income_period(USER, portfolio_returns, accumulation_array, optimal_withdrawal)

        optimal_withdrawal -= 1

    print("")
    print("You can withdrawal $ {:0,.2f}".format(optimal_withdrawal/12), "per month in retirement. Projected success: ", "{:0,.2f}".format(successRate*100)+"%")
    

    return optimal_withdrawal, successRate

if __name__ == '__main__':
    user1 = User(currentAge=25, retirementAge=65, horizonAge=100, riskTolerance="MODERATE", startingBalance=75000, yearlySavings=25000, target_successRate=.85)
    portfolio_returns = get_portfolio_returns(user1)
    accum_res, accumulation_array = calculate_accumulation_period(user1, portfolio_returns)
    optimal_withdrawal, successRate = optimizer(user1, portfolio_returns, accumulation_array)




