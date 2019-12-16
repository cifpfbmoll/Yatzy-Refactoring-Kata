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
        PAR = 2
        for dice in dices:
            if dices.count(dice) >= PAR:
                if lista.count(dice) == 0:
                    lista.append(dice)
                else:
                    continue

        if lista == []:
            return 0
        else:
            if len(lista) >= PAR:
                lista.sort()
                total = (lista[-1] * 2) + (lista[-2] * 2)    
                return total
            else:
                return 0

    
    @staticmethod
    def four_of_a_kind(*dices):
        lista = []
        QUARTET = 4
        for dice in dices:
            if dices.count(dice) >= QUARTET:
                if lista.count(dice) == 0:
                    lista.append(dice)
                else:
                    continue

        if lista == []:
            return 0
        else:
            lista.sort()
            total = (lista[-1] * QUARTET)
            return total

    

    @staticmethod
    def three_of_a_kind(*dices):
        lista = []
        TRIO = 3
        for dice in dices:
            if dices.count(dice) >= TRIO:
                if lista.count(dice) == 0:
                    lista.append(dice)
                else:
                    continue

        if lista == []:
            return 0
        else:
            lista.sort()
            total = (lista[-1] * TRIO)            
            return total
    

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
    def fullHouse(*dices):
        if Yatzy.one_pair(*dices) and Yatzy.three_of_a_kind(*dices):
            total = Yatzy.three_of_a_kind(*dices) + Yatzy.one_pair(*dices)
            return total
        else:
            return 0

    @staticmethod
    def one_pair(*dices):
        PAR = 2
        for dice in dices:
            if dices.count(dice) == PAR:
                total = dice * PAR
                return total

