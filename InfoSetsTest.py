import InfoSets as Is

iSet = Is.InfoSets()

print(iSet.get_info_set('AcAdKsKhBBBBCC5c4d3dBBFF').get_key() == 'AcAdBBBBCC3d4d5cBBFF')
print(iSet.get_info_set('AdAcKsKhBBBBCC5c3d4dBBFF').get_key() == 'AcAdBBBBCC3d4d5cBBFF')
print(iSet.get_info_set('AdAcKsKh').get_key() == 'AcAd')
print(iSet.get_info_set('AdAcKsKhFF').get_key() == 'AcAdFF')
print(iSet.get_info_set('AdAcKsKhFF').get_key() == 'AcAdFF')

print(len(iSet.info_set_list) == 3)