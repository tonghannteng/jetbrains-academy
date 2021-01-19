from random import randint


class CreditCard:
    DEFAULT = 0000
    IIN = 400000

    def __init__(self):
        self.card = ""
        self.pin = self.DEFAULT
        self.word = ""

    def generate_card(self):
        self.word = str(randint(0000000000, 9999999999))
        self.word = "0" * (10 - len(self.word)) + self.word
        self.card = str(self.IIN) + self.word
        self.pin = str(randint(0000, 9999))
        self.pin = "0" * (4 - len(self.pin)) + self.pin
        print("Your card has been created")
        return self.card, self.pin

    def show_credential(self):
        print('Your card number:')
        print(self.card)
        print('Your card PIN:')
        print(self.pin)


creditCardDic = {}
first_flag = True
second_flag = True

while first_flag:

    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")

    option = input('>')

    if option == '0':
        first_flag = False
        print("Bye!")

    if option == '1':
        my_card = CreditCard()
        cardId, pinID = my_card.generate_card()
        creditCardDic[cardId] = pinID
        my_card.show_credential()

    if option == '2':
        print('Enter your card number:')
        card_number = input()
        print('Enter your PIN:')
        pin_number = input()

        if card_number in creditCardDic.keys():
            if creditCardDic[card_number] == pin_number:
                print('You have successfully logged in!')

                while second_flag:
                    print("1. Balance")
                    print("2. Log Out")
                    print("0. Exit")

                    opt = input()
                    if opt == "1":
                        print('Balance: 0')
                    elif opt == "2":
                        print('You have successfully logged out!')
                        second_flag = False
                    elif opt == '0':
                        first_flag = False
                        second_flag = False
                        print("Bye!")
            else:
                print("Wrong card number or PIN!")
        else:
            print("Wrong card number or PIN!")
