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

def parse_history(h):
    if len(h)==0:
        return ("","","")
    elif len(h)<5:
        return (h,"","")
    elif len(h)<9:
        return (h[0:4],h[4:],"")
    h1 = h[0:4]
    h2 = h[4:8]
    preflop = ""
    flop = ""
    round = "preflop"
    actions = ["cc","bb","ff"]
    for i in range(8,len(h),2):
        if h[i:i+2] in actions:
            if round == "preflop":
                preflop += h[i:i+2]
            elif round == "flop":
                flop += h[i:i+2]
        else:
            h1 += h[i:i+2]
            h2 += h[i:i+2]
            round = "flop"
    return (h1,h2,preflop,flop)

def utility(h):
    h1,h2,preflop,flop = parse(h)
    pot = [0.0,0.0]
    player = 0
    bets = 0
    for i in range(0,len(preflop),2):
        if preflop[i:i+2] == "ff":
            s = sum(pot)
            return [s,-s] if player == 1 else [-s,s]
        elif preflop[i:i+2] == "cc":
            pot[player] = pot[1-player]
            player = 1-player
        elif preflop[i:i+2] == "bb":
            pot[player] = pot[1-player]+1.0
            player = 1-player

    player = 0
    terminal = False
    bets = 0
    for i in range(0,len(flop),2):
        if flop[i:i+2] == "ff":
            s = sum(pot)
            return [s,-s] if player == 1 else [-s,s]
        elif flop[i:i+2] == "bb":
            pot[player] = pot[1-player]+1.0
            player = 1-player
            bets += 1
        elif flop[i:i+2] == "cc":
            pot[player] = pot[1-player]
            player = 1-player
            terminal = True

    if bets == 8 or terminal:
        winner = compare_strength(h1,h2)
        s = sum(pot)
        if winner == 0:
            return [s/2.0,s/2.0]
        else:
            return [s,-s] if winner == 1 else [-s,s]

def player(h):
    #returns 0 for chance node, 1,2 for player otherwise
    h1,h2,preflop,flop = parse_history(h)
    if len(h1)!=4 or len(h2)!=4 or len(h1)!=10:
        return 0

    if flop == ""::
        return (len(preflop)/2 %2)+1
    else:
        return (len(flop)/2 %2)+1

def is_terminal(h):
    _,_,preflop,flop = parse_history(h)
    return preflop[-2:]=="ff" or flop[-2:]=="cc" or flop[-2:]=="ff" or len(flop)==16

CARDS=range(52)

def int_to_card(self,x):
    suite = x % 4
    face = x / 4
    return hex(face)[2] + str(suite)

def shuffle_cards():
    shuffle(CARDS)

def deal_cards(x):
    s = ""
    if x == 1:
        for i in range(4):
            s += int_to_card(CARDS[i:i+2])
    elif x == 2:
        for i in range(4,7):
            s += int_to_card(CARDS[i:i+2])
    return s
