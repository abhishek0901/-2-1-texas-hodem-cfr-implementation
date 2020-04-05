class RegretTable:
    def __init__(self):
        self.regret_table = {}

    def add_regrets(self,info_set,action,regret):
        key = (info_set,action)

        if key not in self.regret_table:
            self.regret_table[key] = 0

        self.regret_table[key] += regret

    def get_regrets(self,info_set,action):
        key = (info_set, action)

        if key not in self.regret_table:
            self.regret_table[key] = 0

        return self.regret_table[key]