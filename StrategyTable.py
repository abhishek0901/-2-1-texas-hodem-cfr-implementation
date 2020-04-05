class StrategyTable:
    def __init__(self):
        self.strategy_table = {}

    def add_strategy(self,info_set,action,regret):
        key = (info_set,action)

        if key not in self.strategy_table:
            self.strategy_table[key] = 0

        self.strategy_table[key] += regret

    def get_strategy(self,info_set,action):
        key = (info_set, action)

        if key not in self.strategy_table:
            self.strategy_table[key] = 0

        return self.strategy_table[key]