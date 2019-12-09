class Yatzy:

    @staticmethod
    def chance(*dices):
        total = 0
        for dice in dices:
            total += dice
        return total

    @staticmethod
    def yatzy(dice):
        for die in dice:
            value = dice[0]
            value -= die
            if value != 0:
                return 0
        return 50

    @staticmethod
    def ones(*dices):
        total = 0
        ONE = 1
        for dice in dices:
            if dice == ONE:
                total += dice
        return total

    @staticmethod
    def twos(*dices):
        total = 0
        TWO = 2
        for dice in dices:
            if dice == TWO:
                total += dice
        return total

    @staticmethod
    def threes(*dices):
        total = 0
        THREE = 3
        for dice in dices:
            if dice == THREE:
                total += dice
        return total

    def __init__(self, d1, d2, d3, d4, _5):
        self.dice = [0]*5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5

    def fours(*dices):
        total = 0
        FOUR = 4
        for dice in dices:
            if dice == FOUR:
                total += dice
        return total

    def fives(*dices):
        total = 0
        FIVE = 5
        for dice in dices:
            if dice == FIVE:
                total += dice
        return total

    def sixes(*dices):
        total = 0
        SIX = 6
        for dice in dices:
            if dice == SIX:
                total += dice
        return total

    @staticmethod
    def score_pair(*dices):
        lista = []

        for dice in dices:
            if dices.count(dice) > 1:
                if lista.count(dice) == 0:
                    lista.append(dice)
                else:
                    continue

        if lista == []:
            return 0
        else:
            lista.sort()
            total = lista[-1] * 2    
            return total

    @staticmethod
    def two_pair(*dices):
        lista = []
        
        for dice in dices:
            if dices.count(dice) > 1:
                if lista.count(dice) == 0:
                    lista.append(dice)
                else:
                    continue

        if lista == []:
            return 0
        else:
            lista.sort()
            if len(lista) >= 2:
                total = (lista[-1] * 2) + (lista[-2] * 2)    
                return total
            else:
                return 0

    
    @staticmethod
    def four_of_a_kind( _1,  _2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[_1-1] += 1
        tallies[_2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i+1) * 4
        return 0
    

    @staticmethod
    def three_of_a_kind( d1,  d2,  d3,  d4,  d5):
        t = [0]*6
        t[d1-1] += 1
        t[d2-1] += 1
        t[d3-1] += 1
        t[d4-1] += 1
        t[d5-1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i+1) * 3
        return 0
    

    @staticmethod
    def smallStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[0] == 1 and
            tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1):
            return 15
        return 0
    

    @staticmethod
    def largeStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1
            and tallies[5] == 1):
            return 20
        return 0
    

    @staticmethod
    def fullHouse( d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2): 
                _2 = True
                _2_at = i+1
            

        for i in range(6):
            if (tallies[i] == 3): 
                _3 = True
                _3_at = i+1
            

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
