import numpy as np
import random
from portfolio_allocations import getAllocation
from persona_data import User


def get_market_returns(simulations, Years):

    T = Years # in years


    stock_mkt_expected_return = .085
    stock_mkt_stDev = .15

    bond_mkt_expected_return = .04 #check this
    bond_mkt_expected_stDev = .08 #check this

    
    np.random.seed(6) # using a seed to make sure simulation doesnt change for the same inputs.

    stk_mc = []
    for year in range(T):
        
        year_sim = [] 
        for s in range(simulations):
            sim_return = np.random.normal(stock_mkt_expected_return, stock_mkt_stDev)
            year_sim.append(sim_return)
        
        stk_mc.append(year_sim)

    stock_returns = np.array(stk_mc).T

    bnd_mc = []
    for year in range(T):
        
        year_sim = [] 
        for s in range(simulations):
            sim_return = np.random.normal(bond_mkt_expected_return, bond_mkt_expected_stDev)
            year_sim.append(sim_return)
        
        bnd_mc.append(year_sim)

    bond_returns = np.array(bnd_mc).T

    return stock_returns, bond_returns

def get_portfolio_returns(USER):
    stk_ret, bnd_ret = get_market_returns(1000, USER.totalYears)
    allocation = getAllocation(USER.riskTolerance)

    for yr in range(USER.totalYears):
        portfolio_returns = stk_ret[:,yr]*allocation["stock_allocation"] + bnd_ret[:,yr]*allocation['bond_allocation']

        if yr == 0:
            portfolio_array = portfolio_returns
        
        else:
            portfolio_array = np.column_stack((portfolio_array,portfolio_returns))

    portfolio_returns_array = portfolio_array

    return portfolio_returns_array

if __name__ == '__main__':
    user1 = User(25, 65, 100, "MODERATE", 100000, 2500)
    portfolio_returns_array = get_portfolio_returns(user1)
    
    

print("")