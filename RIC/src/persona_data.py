# defining a the user class.

class User:
    def __init__(self, currentAge, retirementAge, horizonAge, riskTolerance, startingBalance, yearlySavings, target_successRate):
        # in years
        self.currentAge = currentAge
        self.retirementAge = retirementAge
        self.horizonAge = horizonAge
        self.riskTolerance = riskTolerance #VERY_CONSERVATIVE, CONSERVATIVE, MODERATE, AGGRESSIVE, VERY_AGGRESSIVE

        self.accumulationYears = retirementAge - currentAge + 1
        self.incomeYears = horizonAge - retirementAge

        self.startingBalance = startingBalance
        self.yearlySavings = yearlySavings # only in accumulation years.

        self.totalYears = horizonAge - currentAge + 1
        self.target_successRate = target_successRate

