class StrategyTable:
    def __init__(self):
        self.strategy_table = {}
        self.strategy_table_frequency = {}

    def add_strategy(self,info_set,action,regret):
        key = (info_set,action)

        if key not in self.strategy_table:
            self.strategy_table[key] = 0
            self.strategy_table_frequency[key] = 0

        self.strategy_table_frequency[key] += 1
        self.strategy_table[key] = self.strategy_table[key]*(self.strategy_table_frequency[key] -1)/self.strategy_table_frequency[key] +\
                                   regret / self.strategy_table_frequency[key]

    def get_strategy(self,info_set,action):
        key = (info_set, action)

        if key not in self.strategy_table:
            self.strategy_table[key] = 0

        return self.strategy_table[key]