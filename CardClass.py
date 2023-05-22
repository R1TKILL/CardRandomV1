
class Cards:
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

    def informations(self):
        print("\n"
              "*************************************************************\n"
              "                        Card Value                           \n"
              f" *Value.....................:   ${self.value}               \n"
              f" *Suit......................:   ${self.suit}                \n"
              "*************************************************************\n"
              "\n")