#single,multiple,multi level,hierachy,hybrid
class whatsappv1:
    def __init__(self,name):
        self.name = name
        print(f"Welcome to the whatsapp - v1 {self.name}!")
    def messaging(self):
        print("You can send messages")
class whatsappV2(whatsappv1):
    def __init__(self, name):
       self.name = name
       print(f"Welcome to the whatsapp - v2 {self.name}!")
    def calls(self):
        print("You can audio and video calls")

chandra = whatsappv1('chandra')
chandra.messaging()

suhi = whatsappV2('suhi')
suhi.messaging()
suhi.calls()

