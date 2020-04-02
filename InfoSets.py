#Implement list of InfoSet
import InfoSet as infoSet

class InfoSets:

    def __init__(self):
        self.info_set_list = {}
        self.allPosiibleAction = ['B', 'C', 'F']

    def extract_key_from_history(self,h):
        key = []
        new_h = h[0:4] + h[8:] if len(h) > 4 else 0
        c1 = new_h[0:2]
        c2 = new_h[2:4]

        key.append(c1)
        key.append(c2)

        key = sorted(key)
        next_chance = 4
        sorted_key = []
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

        sorted_key = sorted(sorted_key)
        key.append(pre_flop_actions)
        key.append("".join(sorted_key))
        if next_chance != len(new_h):
            key.append(new_h[next_chance+6 : ])

        return "".join(key)

    def get_info_set(self,h):
        key = self.extract_key_from_history(h)

        if key not in self.info_set_list:
            info_set = infoSet.InfoSet(key)
            self.info_set_list[key] = info_set

        return self.info_set_list[key]