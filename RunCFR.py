import CFR as cfr
import Poker as poker
import InfoSets as infoSets
import RegretTable as regretTable
import StrategyTable as strategyTable
import StrategyProfile as stratgeyProfile
import pickle
import os
from os import path

class RunCFR:

    def __init__(self,dir_name=''):
        self.dir_name = dir_name
        self.players = [1,2]
        self.poker = poker.Poker()
        self.crt = "cumulative_regret_table.obj"
        self.cst = "cumulative_strategy_table.obj"
        self.sp = "strategy_profile.obj"
        self.inofosset = "info_sets.obj"

        if not path.exists(dir_name):
            self.info_sets = infoSets.InfoSets()
            self.cumulative_regret_table = regretTable.RegretTable()
            self.cumulative_strategy_table = strategyTable.StrategyTable()
            self.strategy_profile = stratgeyProfile.StrategyProfile()
        else:
            file = open(dir_name + '/' + self.crt, 'r')
            self.cumulative_regret_table = pickle.load(file)

            file = open(dir_name + '/' + self.cst, 'r')
            self.cumulative_strategy_table = pickle.load(file)

            file = open(dir_name + '/' + self.sp, 'r')
            self.strategy_profile = pickle.load(file)

            file = open(dir_name + '/' + self.inofosset, 'r')
            self.info_sets = pickle.load(file)



        self.cfr = cfr.CFR(self.poker,self.cumulative_regret_table,self.cumulative_strategy_table,self.strategy_profile,self.info_sets)

    def run_cfr(self,iterations):
        for iter in range(iterations):
            for i in self.players:
                self.cfr.run_cfr('',i,iter,1,1)

            if iter % 1 == 0:
                dir_name = 'weights_' + str(iter)
                os.makedir(dir_name)

                file = open(dir_name + '/' + self.crt,'w')
                pickle.dump(self.cumulative_regret_table,file)

                file = open(dir_name + '/' + self.cst, 'w')
                pickle.dump(self.cumulative_strategy_table,file)

                file = open(dir_name + '/' + self.sp, 'w')
                pickle.dump(self.strategy_profile,file)

                file = open(dir_name + '/' + self.inofosset, 'w')
                pickle.dump(self.info_sets,file)


# Running CFR
run_cfr = RunCFR()
run_cfr.run_cfr(10)