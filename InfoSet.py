# This creates a node info set
#Assumption First time this method is called after 4 cards dealt
class InfoSet:
    def __init__(self,key):
        self.allPosiibleAction = ['B','C','F']
        self.key = key

    def get_key(self):
        return self.key

    def get_actions(self):
        if self.key[-1] == 'F':
            return []
        elif self.key[-1] not in self.allPosiibleAction:
            return ['B','F']
        else:
            return self.allPosiibleAction