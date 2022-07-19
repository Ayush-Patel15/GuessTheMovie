# Creatin a basic Player: with all common properties

class Player(object):

    def __init__(self,name) -> None:
        self.name = name
        self.prize_money = 500
        self.prizes_lst = []
        self.prison_charge = 100

    def add_prize_money(self, amount):
        self.prize_money = self.prize_money + amount

    def add_prize_lst(self,prize):
        self.prizes_lst.append(prize)

    def prison(self):
        self.prize_money = self.prize_money - self.prison_charge

    def __str__(self) -> str:
        return "{0}, has ${1} /-".format(self.name, self.prize_money)


class HumanPlayer(Player):
    
    def human_get_move(self):
        letter = input("Enter your guess: ").upper()
        return letter


if __name__ == "__main__":
    obj1 = Player(name="Ayush")
    print(obj1.__str__())

    # obj2 = HumanPlayer(name="Bittu")
    # print(obj2.human_get_move())
    # print(obj2.__str__())
