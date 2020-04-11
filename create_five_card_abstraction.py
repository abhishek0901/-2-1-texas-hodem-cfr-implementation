import InfosetAbstraction as infoset

# Data Source : http://archive.ics.uci.edu/ml/datasets/Poker+Hand

######### Five Card Abstraction STARTS #########################

info_set = infoset.InfosetAbstraction()
data  = info_set.prepare_data('poker-hand-training-true.csv')
info_set.run_k_means(data,999)
info_set.save_model("five_card_abstraction.obj")

######### Five Card Abstraction ENDS ###########################

######### TWO Card Abstraction STARTS ##########################

info_set = infoset.InfosetAbstraction()
data  = info_set.prepare_data_two_card('poker-hand-training-true.csv')
info_set.run_k_means(data,169)
info_set.save_model("two_card_abstraction.obj")

######### TWO Card Abstraction ENDS ############################