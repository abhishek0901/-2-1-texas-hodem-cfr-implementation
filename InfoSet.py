# This creates a node info set
#Assumption First time this method is called after 4 cards dealt
class InfoSet:
    def __init__(self,key):
        self.allPosiibleAction = ['BB','CC','FF']
        self.key = key

    def get_key(self):
        return self.key

    def get_actions(self):
        if self.key[-2:] == 'FF':
            return []
        elif self.key[-2:] not in self.allPosiibleAction:
            return ['BB','FF']
        else:
            return self.allPosiibleAction