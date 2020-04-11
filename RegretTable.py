class RegretTable:
    def __init__(self):
        self.regret_table = {}
        self.regret_table_frequency = {}

    def add_regrets(self,info_set,action,regret):
        key = (info_set,action)

        if key not in self.regret_table:
            self.regret_table[key] = 0
            self.regret_table_frequency[key] = 0

        self.regret_table_frequency[key] += 1
        self.regret_table[key] = self.regret_table[key] * (self.regret_table_frequency[key]-1)/self.regret_table_frequency[key] \
                                 + regret / self.regret_table_frequency[key]

    def get_regrets(self,info_set,action):
        key = (info_set, action)

        if key not in self.regret_table:
            self.regret_table[key] = 0

        return self.regret_table[key]