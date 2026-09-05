from abc import ABC, abstractmethod

class Phonepay(ABC):

    def senderinfo(self):
        print("You can enter their mobile number or scanner")

    def amount(self):
        print("You can enter amount")

    def pin(self):
        print("You need to enter the pin")

    @abstractmethod
    def transaction(self):
        pass


class HDFC(Phonepay):
    def transaction(self):
        print("Payment using HDFC bank")


class UNION(Phonepay):
    def transaction(self):
        print("Payment using Union bank")


class AXIS(Phonepay):
    def transaction(self):
        print("Payment using Axis bank")


class ICIC(Phonepay):
    def transaction(self):
        print("Payment using ICIC bank")


chandra = HDFC()
chandra.senderinfo()
chandra.amount()
chandra.pin()
chandra.transaction()

vaishu = UNION()
vaishu.senderinfo()
vaishu.amount()
vaishu.pin()
vaishu.transaction()

gayi = AXIS()
gayi.senderinfo()
gayi.amount()
gayi.pin()
gayi.transaction()

suhi = ICIC()
suhi.senderinfo()
suhi.amount()
suhi.pin()
suhi.transaction()