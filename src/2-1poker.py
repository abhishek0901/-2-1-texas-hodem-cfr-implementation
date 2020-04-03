from random import shuffle

#for ease of implementation, cards are labelled in 13-nary numbers
#0,1,2,3,4,5,6,7,8,9,a,b,c
#every card is a two symbol
#the first symbol is the face, the second is the suite
#0,1,2,3 are diamonds, clubs, hearts, spades
#for example, 32 is the 4 of hearts

#rules implemented according to
#https://www.pagat.com/poker/rules/ranking.html

def all_same(L):
    #check if all entries of vector L are the same
    #if same, return (true,L[0]), else return false
    for i in range(1,len(L)):
        if L[i]!=L[i-1]:
            return False
    return True

#TODO: this function does not yet implement wheel for straights yet
def compare_strength(h1,h2):
    #input hands as strings
    #return 0 if hands are equal
    #else return 1 or 2
    h1_tmp=[(int(h1[2*i],16),int(h1[2*i+1])) for i in range(5)]
    h1_tmp.sort()
    h1_faces=[i[0] for i in h1_tmp]
    h1_suites=[i[1] for i in h1_tmp]
    h2_tmp=[(int(h2[2*i],16),int(h2[2*i+1])) for i in range(5)]
    h2_tmp.sort()
    h2_faces=[i[0] for i in h2_tmp]
    h2_suites=[i[1] for i in h2_tmp]

    #make sure h1 and h2 are different
    if h1_tmp==h2_tmp:
        return 0

    #check for straight flush
    h1_straight_flush=True
    for i in range(1,5):
        if h1_suites[i]!= h1_suites[i-1] or h1_faces[i]-h1_faces[i-1]!=1:
            h1_stright_flush=False
            break

    h2_straight_flush=True
    for i in range(1,5):
        if h2_suites[i]!= h2_suites[i-1] or h2_faces[i]-h2_faces[i-1]!=1:
            h2_stright_flush=False
            break

    if h1_straight_flush and not h2_straight_flush:
        return 1
    elif h2_straight_flush and not h1_straight_flush:
        return 2
    elif h1_straight_flush and h2_straight_flush:
        return (h2_faces[4] > h1_faces[4])+1

    #check for four of a kind
    h1_four_of_a_kind = all_same(h1_faces[0:4]) or all_same(h1_faces[1:5])
    h2_four_of_a_kind = all_same(h2_faces[0:4]) or all_same(h2_faces[1:5])
    if h1_four_of_a_kind and not h2_four_of_a_kind:
        return 1
    elif not h1_four_of_a_kind and h2_four_of_a_kind:
        return 2
    elif h1_four_of_a_kind and h2_four_of_a_kind:
        if h1_faces == h2_faces:
            return 0
        elif h1_faces[2]!=h2_faces[2]:
            return (h2_faces[2]>h1_faces[2])+1
        else:
            h1_kicker = h1_faces[4] if h1_faces[4]!=h1_faces[2] else h1_faces[0]
            h2_kicker = h2_faces[4] if h2_faces[4]!=h2_faces[2] else h2_faces[0]
            return (h2_kicker > h1_kicker)+1

    #check for full house
    h1_fullhouse = all_same(h1_faces[0:2]) and all_same(h1_faces[2:5])
    h2_fullhouse = all_same(h2_faces[0:2]) and all_same(h2_faces[2:5])
    if h1_fullhouse and not h2_fullhouse:
        return 1
    elif h2_fullhouse and not h1_fullhouse:
        return 2
    elif h1_fullhouse and h2_fullhouse:
        if h1_faces == h2_faces:
            return 0
        elif h1_faces[2] != h2_faces[2]:
            return (h2_faces[2] > h1_faces[2])+1
        else:
            h1_rank = h1_faces[4] if h1_faces[4]!=h1_faces[2] else h1_faces[0]
            h2_rank = h2_faces[4] if h2_faces[4]!=h2_faces[2] else h2_faces[0]
            return (h2_rank > h1_rank)+1

    #check for flush
    h1_flush = all_same(h1_suites)
    h2_flush = all_same(h2_suites)
    if h1_flush and not h2_flush:
        return 1
    elif h2_flush and not h1_flush:
        return 2
    elif h1_flush and h2_flush:
        if h1_faces == h2_faces:
            return 0
        else:
            for i in [4,3,2,1,0]:
                if h1_faces[i] != h2_faces[i]:
                    return (h2_faces[i] > h1_faces[i])+1

    #check for straight
    h1_straight = True
    for i in range(1,5):
        if h1_faces[i]-h1_faces[i-1]!=1:
            h1_straight = False
            break
    h2_straight = True
    for i in range(1,5):
        if h2_faces[i]-h2_faces[i-1]!=1:
            h2_straight = False
            break
    if h1_straight and not h2_straight:
        return 1
    elif h2_straight and not h1_straight:
        return 2
    elif h1_straight and h2_straight:
        return (h2_faces[4] > h1_faces[4])+1

    #check for 3 of a kind
    h1_three_of_a_kind = all_same(h1_faces[0:3]) or all_same(h1_faces[1:4]) or all_same(h1_faces[2:5])
    h2_three_of_a_kind = all_same(h2_faces[0:3]) or all_same(h2_faces[1:4]) or all_same(h2_faces[2:5])
    if h1_three_of_a_kind and not h2_three_of_a_kind:
        return 1
    elif h2_three_of_a_kind and not h1_three_of_a_kind:
        return 2
    elif h1_three_of_a_kind and h2_three_of_a_kind:
        if h1_faces == h2_faces:
            return 0
        elif h1_faces[2] != h2_faces[2]:
            return (h2_faces[2] > h1_faces[2])+1
        else:
            if all_same(h1_faces[0:3]):
                h1_rank = (h1_faces[4],h1_faces[3])
            elif all_same(h1_faces[1:4]):
                h1_rank = (h1_faces[4],h1_faces[0])
            else:
                h1_rank = (h1_faces[1],h1_faces[0])

            if all_same(h2_faces[0:3]):
                h2_rank = (h2_faces[4],h2_faces[3])
            elif all_same(h2_faces[1:4]):
                h2_rank = (h2_faces[4],h2_faces[0])
            else:
                h2_rank = (h2_faces[1],h2_faces[0])

            return (h2_rank > h1_rank)+1

    #check for two pairs
    h1_two_pairs = (all_same(h1_faces[0:2]) and all_same(h1_faces[2:4])) or
                   (all_same(h1_faces[0:2]) and all_same(h1_faces[3:5])) or
                   (all_same(h1_faces[1:3]) and all_same(h1_faces[3:5]))
    h2_two_pairs = (all_same(h2_faces[0:2]) and all_same(h2_faces[2:4])) or
                   (all_same(h2_faces[0:2]) and all_same(h2_faces[3:5])) or
                   (all_same(h2_faces[1:3]) and all_same(h2_faces[3:5]))
    if h1_two_pairs and not h2_two_pairs:
        return 1
    elif h2_two_pairs and not h1_two_pairs:
        return 2
    elif h1_two_pairs and h2_two_pairs:
        if h1_faces == h2_faces:
            return 0

        if all_same(h1_faces[3:5]) and all_same(h1_faces[1:3]):
            h1_rank = (h1_faces[3],h1_faces[1],h1_faces[0])
        elif all_same(h1_faces[3:5]) and all_same(h1_faces[0:2]):
            h1_rank = (h1_faces[3],h1_faces[1],h1_faces[2])
        elif all_same(h1_faces[2:4]) and all_same(h1_faces[0:2]):
            h1_rank = (h1_faces[3],h1_faces[1],h1_faces[4])

        if all_same(h2_faces[3:5]) and all_same(h2_faces[1:3]):
            h2_rank = (h2_faces[3],h2_faces[1],h2_faces[0])
        elif all_same(h2_faces[3:5]) and all_same(h2_faces[0:2]):
            h2_rank = (h2_faces[3],h2_faces[1],h2_faces[2])
        elif all_same(h2_faces[2:4]) and all_same(h2_faces[0:2]):
            h2_rank = (h2_faces[3],h2_faces[1],h2_faces[4])

        return (h2_rank > h1_rank)+1

    #check for pair
    h1_pair = all_same(h1_faces[0:2]) or all_same(h1_faces[1:3]) or
              all_same(h1_faces[2:4]) or all_same(h1_faces[3:5])
    h2_pair = all_same(h2_faces[0:2]) or all_same(h2_faces[1:3]) or
              all_same(h2_faces[2:4]) or all_same(h2_faces[3:5])
    if h1_pair and not h2_pair:
        return 1
    elif h2_pair and not h1_pair:
        return 2
    elif h1_pair and h2_pair:
        if h1_faces == h2_faces:
            return 0

        if all_same(h1_faces[0:2]):
            h1_rank = (h1_faces[0],h1_faces[4],h1_faces[3],h1_faces[2])
        elif all_same(h1_faces[1:3]):
            h1_rank = (h1_faces[1],h1_faces[4],h1_faces[3],h1_faces[0])
        elif all_same(h1_faces[2:4]):
            h1_rank = (h1_faces[2],h1_faces[4],h1_faces[1],h1_faces[0])
        elif all_same(h1_faces[3:5]):
            h1_rank = (h1_faces[3],h1_faces[2],h1_faces[1],h1_faces[0])

        if all_same(h2_faces[0:2]):
            h2_rank = (h2_faces[0],h2_faces[4],h2_faces[3],h2_faces[2])
        elif all_same(h2_faces[1:3]):
            h2_rank = (h2_faces[1],h2_faces[4],h2_faces[3],h2_faces[0])
        elif all_same(h2_faces[2:4]):
            h2_rank = (h2_faces[2],h2_faces[4],h2_faces[1],h2_faces[0])
        elif all_same(h2_faces[3:5]):
            h2_rank = (h2_faces[3],h2_faces[2],h2_faces[1],h2_faces[0])

        return (h2_rank > h1_rank)+1

    #check if nothing
    if h1_faces == h2_faces:
        return 0
    else:
        for i in [4,3,2,1,0]:
            if h1_faces[i] != h2_faces[i]:
                return (h2_faces[i] > h1_faces[i])+1

def symbol_translator(s):
    if s[1]=='9':
        face = 'jack'
    elif s[1]=='a':
        face = 'queen'
    elif s[1]=='b':
        face = 'king'
    elif s[1]=='c':
        face = 'ace'
    else:
        face = str(int(s[1]) + 2)

    suite = ['diamonds','clubs','hearts','spades'][int(s[0])]
    return face + " of " + suite

class two_one_poker:

    def __init__(self):
        self.round = "preflop"
        self.tmp = range(52)
        shuffle(tmp)
        '''
        self.p1_private = self.int_to_card(tmp[0]) + self.int_to_card(tmp[1])
        self.p2_private = self.int_to_card(tmp[2]) + self.int_to_card(tmp[3])
        self.public_cards = self.int_to_card(tmp[4]) + self.int_to_card(tmp[5]) + self.int_to_card(tmp[6])
        '''
        self.preflop_actions = ""
        self.flop_actions = ""
        self.pot = [0.0,0.0]
        self.terminal = False

    def int_to_card(self,x):
        suite = x % 4
        face = x / 4
        return hex(face)[2] + str(suite)

    def get_infoset(self,player):
        if self.round == "preflop":
            if player == 1:
                l = self.tmp[0:2]
            elif player == 2:
                l = self.tmp[2:4]
            actions = self.preflop_actions
        elif self.round == "flop":
            if player == 1:
                l = self.tmp[0:2] + self.tmp[4:7]
            elif player == 2:
                l = self.tmp[2:7]
            actions = self.flop_actions
        l.sort()
        s = ""
        for i in l:
            s += self.int_to_card(i)
        return s + actions

    def get_player(self):
        if self.round == "preflop":
            return (len(self.preflop_actions)/2 % 2)+1
        elif self.round == "flop":
            return (len(self.flop_actions)/2 % 2)+1

    def get_actions(self):
        if self.terminal:
            return []
        elif self.round == "preflop":
            if self.preflop_actions == "":
                return ["bb","ff"]
            else:
                return ["bb","cc","ff"]
        elif self.round == "flop":
            if self.flop_actions == "" and self.p1_pot < self.p2_pot:
                return ["bb","ff"]
            else:
                return ["bb","cc","ff'"]

    def play_action(self,a):
        if a in self.get_actions():
            if self.round == "preflop":
                if a == "ff":
                    self.terminal = True
                elif a == "cc":
                    self.pot[self.get_player()] += 1.0
                    self.round = "flop"
                elif a == "bb":
                    self.pot[self.get_player()] += 1.0 if self.preflop_actions == "" else 2.0
                    if self.preflop_actions == "b"*14:
                        self.round == "flop"
                self.preflop_actions += a
            elif self.round == "flop":
                if a == "ff":
                    self.terminal = True
                elif a == "cc":
                    self.pot[self.get_player()] += 1.0
                    self.terminal = True
                elif a == "bb":
                    self.pot[self.get_player()] += 1.0 if self.flop_actions == "" else 2.0
                    if self.flop_actions =="b"*14:
                        self.terminal = True
                self.flop_actions += a

    def is_terminal(self):
        return self.terminal

    def result(self):
        if not self.terminal:
            return (0.0,0.0)
        elif self.round == "preflop":
            if self.get_player() == 1: #this means p2 folded
                return (sum(self.pot),-sum(self.pot))
            else:
                return (-sum(self.pot),sum(self.pot))
        elif self.flop_actions[-2:] == "ff":
            if self.get_player() == 1: #this means p2 folded
                return (sum(self.pot),-sum(self.pot))
            else:
                return (-sum(self.pot),sum(self.pot))
        else:
            h1 = self.get_infoset(1)[0:11]
            h2 = self.get_infoset(2)[0:11]
            winner = compare_strength(h1,h2)
            s = sum(self.pot)
            if winner == 0:
                return (s/2.0,s/2.0)
            else:
                return (s,-s) if winner == 1 else (-s,s)
