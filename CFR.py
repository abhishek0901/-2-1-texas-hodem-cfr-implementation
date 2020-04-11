# This implements Counter factual regret minimization

# CFR -> h = AdAcKhkc

class CFR:

    #Initialize CFR with all important variables
    def __init__(self,poker,cumulative_regret_table,cumulative_strategy_table,strategy_profile,info_sets):
        self.poker = poker
        self.cumulative_regret_table = cumulative_regret_table
        self.cumulative_strategy_table = cumulative_strategy_table
        self.strategy_profile = strategy_profile
        self.players = [1,2] # Assumption -> Texas Holdem Poker
        self.info_sets = info_sets

    def run_cfr(self,h,i,t,pi1,pi2):

        if self.poker.is_terminal(h):
            return self.poker.utility(h)[self.poker.player(h)-1]  # Assumption - poker class has to check which player won and should return appropriate utility
        elif self.poker.player(h) not in self.players:
            card = self.poker.deal_cards(h) #poker class should know which round it is in
            return self.run_cfr(h+card,i,t,pi1,pi2)

        info_set = self.info_sets.get_info_set(h,self.poker.player(h))

        v_sigma = 0
        actions = info_set.get_actions()
        v_sigma_infoset = {}
        for a in actions:
            v_sigma_infoset[a] = 0

        for a in actions:
            if self.poker.player(h) == self.players[0]:
                v_sigma_infoset[a] = self.run_cfr(h+a,i,t,
                                                  self.strategy_profile.get_strategy_profile(t,info_set,a) * pi1,pi2)
            elif self.poker.player(h) == self.players[1]:
                v_sigma_infoset[a] = self.run_cfr(h + a, i, t,pi1,
                                                  self.strategy_profile.get_strategy_profile(t, info_set,a) * pi2)

            v_sigma = v_sigma + self.strategy_profile.get_strategy_profile(t,info_set,a) * v_sigma_infoset[a]

        if self.poker.player(h) == i:
            pi_minus_i = pi2 if i == 1 else pi1
            pi_i = pi1 if i == 1 else pi2

            for a in actions:
                self.cumulative_regret_table.add_regrets(info_set.get_key(),a,pi_minus_i * (v_sigma_infoset[a] - v_sigma))
                self.cumulative_strategy_table.add_strategy(info_set.get_key(),a,pi_i * self.strategy_profile.get_strategy_profile(t,info_set,a))

            regret_positive_total = 0
            for a in actions:
                regret_positive_total += self.cumulative_regret_table.get_regrets(info_set,a) if self.cumulative_regret_table.get_regrets(info_set,a) > 0 else 0

            for a in actions:
                if regret_positive_total > 0:
                    regret_positive = self.cumulative_regret_table.get_regrets(info_set,a) if self.cumulative_regret_table.get_regrets(info_set,a) > 0 else 0
                    self.strategy_profile.set_strategy_profile(t + 1, info_set, a, regret_positive / regret_positive_total)
                else:
                    self.strategy_profile.set_strategy_profile(t+1,info_set,a,1.0/len(actions))

        return v_sigma
