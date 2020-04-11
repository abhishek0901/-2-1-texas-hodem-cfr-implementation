#Implement list of InfoSet
import InfoSet as infoSet
import BucketTable as bucket
class InfoSets:

    def __init__(self):
        self.info_set_list = {}
        self.allPosiibleAction = ['B', 'C', 'F']
        self.SUIT = {'hearts':1,'spades':2,'diamonds':3,'clubs':4}
        self.RANK = {'ace':1,'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'jack':11, 'queen':12, 'king':13}
        self.bucket = bucket.BucketTable()

    def extract_key_from_history(self,h,current_player=1):
        key = []
        if current_player == 1:
            new_h = h[0:4] + h[8:] if len(h) > 4 else 0
        else:
            new_h = h[4:8] + h[8:] if len(h) > 4 else 0
        c1 = new_h[0:2]
        c2 = new_h[2:4]

        key.append(c1)
        key.append(c2)

        #key = sorted(key)
        next_chance = 4
        sorted_key = key
        while next_chance < len(new_h) and new_h[next_chance] in self.allPosiibleAction:
            next_chance += 2
        pre_flop_actions = new_h[4:next_chance]
        if next_chance != len(new_h):
            c3 = new_h[next_chance:next_chance+2]
            c4 = new_h[next_chance+2:next_chance+4]
            c5 = new_h[next_chance+4:next_chance+6]

            sorted_key.append(c3)
            sorted_key.append(c4)
            sorted_key.append(c5)

        #sorted_key = sorted(sorted_key)
        #key.append(pre_flop_actions)
        key = sorted(sorted_key)
        sorted_key = []
        for card in key:
            a,b = self.get_data_point(int(card))
            sorted_key.append(a)
            sorted_key.append(b)
        sorted_key = [sorted_key]
        sorted_key = self.bucket.get_bucket_id(sorted_key,1 if len(sorted_key[0]) < 5 else 2)
        sorted_key += pre_flop_actions
        key = sorted_key
        if next_chance != len(new_h):
            key += new_h[next_chance+6 : ]

        return key

    def get_info_set(self,h,current_player):
        key = self.extract_key_from_history(h,current_player)

        if key not in self.info_set_list:
            info_set = infoSet.InfoSet(key)
            self.info_set_list[key] = info_set

        return self.info_set_list[key]

    def get_data_point(self,card):
        face = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace'][int(card / 4)]
        suite = ['diamonds', 'clubs', 'hearts', 'spades'][card % 4]

        return self.SUIT[suite],self.RANK[face]