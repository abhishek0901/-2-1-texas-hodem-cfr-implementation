import InfoSet as info_set

infoSet = info_set.InfoSet("AcAdBBBBCC3d4d5cBBFF")
print(infoSet.get_key() == "AcAdBBBBCC3d4d5cBBFF")

infoSet = info_set.InfoSet("AcAdBBBBCC3d4d5cBBFF")
print(infoSet.get_key() == "AcAdBBBBCC3d4d5cBBFF")

infoSet = info_set.InfoSet("AcAd")
print(infoSet.get_key() == 'AcAd')

infoSet = info_set.InfoSet("AcAdFF")
print(infoSet.get_key() == 'AcAdFF')

infoSet = info_set.InfoSet("AcAdFF")
print(infoSet.get_key() == 'AcAdFF')