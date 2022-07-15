# Creatin a basic Player: with all common properties

class Player(object):

    def __init__(self,name) -> None:
        self.name = name
        self.prize_money = 0
        self.prizes_lst = []

    def add_prize_money(self, amount):
        self.prize_money = self.prize_money + amount

    def add_prize_lst(self,prize):
        self.prizes_lst.append(prize)

    def bankrupt(self):
        self.prize_money = 0

    def __str__(self) -> str:
        return "{0}, has ${1} /-".format(self.name, self.prize_money)

class HumanPlayer(Player):
    pass


class ComputerPlayer(Player):
    pass


if __name__ == "__main__":
    obj = Player(name="Ayush")
    print(obj.__str__())