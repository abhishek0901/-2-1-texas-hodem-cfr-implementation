class StrategyProfile:
    def __init__(self):
        self.strategy_profile = {}

    def set_strategy_profile(self,t,info_set,action,strategy):
        key = (t,info_set.get_key(), action)

        if key not in self.strategy_profile:
            self.strategy_profile[key] = 0

        self.strategy_profile[key] = strategy

    def get_strategy_profile(self,t,info_set,action):
        key = (t,info_set.get_key(), action)

        if key not in self.strategy_profile:
            self.strategy_profile[key] = 1.0 / len(info_set.get_actions())

        return self.strategy_profile[key]