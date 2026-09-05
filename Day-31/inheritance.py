#single 
class whatsappv1:
    def messaging(self):
        print("You can message")
class whatsappv2(whatsappv1):
    def calls(self):
        print("You can audio and video calls")
a = whatsappv1()
a.messaging()
b = whatsappv2()
b.calls()
#multi-level
class whatsappv1:
    def messaging(self):
        print("You can message")
class whatsappv2(whatsappv1):
    def calls(self):
        print("You can audio and video calls")
class whatsappv3(whatsappv2):
    def status(self):
        print("You can add the status for 24 hours")
a = whatsappv1()
a.messaging()

b = whatsappv2()
b.calls()
b.messaging()

c = whatsappv3()
c.messaging()
c.calls()
c.status()
#multiple
class whatsappv1:
    def messaging(self):
        print("You can message")
class whatsappv2:
    def calls(self):
        print("You can audio and video calls")
class whatsappv3(whatsappv1,whatsappv2):
    def status(self):
        print("You can add the status for 24 hours")
a = whatsappv1()
a.messaging()

b = whatsappv2()
b.calls()


c = whatsappv3()
c.messaging()
c.calls()
c.status()

#hierachy

class whatsappv1:
    def messaging(self):
        print("You can message")
class whatsappv2(whatsappv1):
    def calls(self):
        print("You can audio and video calls")
class whatsappv3(whatsappv1):
    def status(self):
        print("You can add the status for 24 hours")
a = whatsappv1()
a.messaging()
b = whatsappv2()
b.calls()
c = whatsappv3()
c.messaging()
c.status()

#hybrid-combination of any two
class whatsappv1:
    def messaging(self):
        print("You can message")

class whatsappv2:
    def extramessage(self):
        print("You can add emojis, stickers and gifs")

class whatsappv3(whatsappv1,whatsappv2):
    def calls(self):
        print("You can audio and video calls")

class whatsappv4(whatsappv3):
    def status(self):
        print("You can add the status for 24 hours")
a = whatsappv1()
a.messaging()

b = whatsappv2()
b.extramessage()

c = whatsappv3()
c.messaging()
c.extramessage()
c.calls()

d = whatsappv4()
d.messaging()
d.extramessage()
d.calls()
d.status()
    
#super()- whenerver there is same methods we use super keyword to acess parents class methods
class whatsappv1():
    def status(self):
        print("You can add images and videos")
class whatsappv2(whatsappv1):
    def status(self):
        super().status()
        print("You can add music and stickers")
class whatsappv3(whatsappv2):
    def status(self):
        super().status()
        print("You can like and you can add reaction")
a = whatsappv3()
a.status()

class whatsappv1:

    def status(self):
        print("You can add images and videos")
#class name

class whatsappv2(whatsappv1):

    def status(self):
        super().status()
        print("You can add music and stickers")


class whatsappv3(whatsappv2):

    def status(self):
        super().status()
        print("You can like and you can add reaction")


a = whatsappv3()

a.status()

#python doesnot support overloading we can use default value

