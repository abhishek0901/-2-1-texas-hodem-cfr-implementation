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
            file = open(dir_name + '/' + self.crt, 'rb')
            self.cumulative_regret_table = pickle.load(file)
            file.close()

            file = open(dir_name + '/' + self.cst, 'rb')
            self.cumulative_strategy_table = pickle.load(file)
            file.close()

            file = open(dir_name + '/' + self.sp, 'rb')
            self.strategy_profile = pickle.load(file)
            file.close()

            file = open(dir_name + '/' + self.inofosset, 'rb')
            self.info_sets = pickle.load(file)
            file.close()



        self.cfr = cfr.CFR(self.poker,self.cumulative_regret_table,self.cumulative_strategy_table,self.strategy_profile,self.info_sets)

    def run_cfr(self,start,iterations):
        for iter in range(start,iterations):
            for i in self.players:
                self.cfr.run_cfr('',i,iter,1,1)


            if iter % 10 == 0:
                dir_name = './weights/weights_' + str(iter)
                os.makedirs(dir_name)

                file = open(dir_name + '/' + self.crt,'wb')
                pickle.dump(self.cumulative_regret_table,file)
                file.close()

                file = open(dir_name + '/' + self.cst, 'wb')
                pickle.dump(self.cumulative_strategy_table,file)
                file.close()

                file = open(dir_name + '/' + self.sp, 'wb')
                pickle.dump(self.strategy_profile,file)
                file.close()

                file = open(dir_name + '/' + self.inofosset, 'wb')
                pickle.dump(self.info_sets,file)
                file.close()


# Running CFR
start = 0
total_iter = 100
directory_to_load = '' # For loading weights input relevant weight folder

run_cfr = RunCFR(directory_to_load)
run_cfr.run_cfr(start,total_iter)