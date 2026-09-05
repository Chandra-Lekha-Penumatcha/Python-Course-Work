# Method overriding:
# Same method, same parameters, different implementation

class Hotstar:

    def __init__(self, name):
        print(f"Welcome to Hotstar, {name}")

    def login(self):
        print("You can login to Hotstar")

    def dashboard(self):
        print("You can see the dashboard")

    def search(self):
        print("You can search")

    def playcontrollers(self):
        print("Pause, Resume, Play")

    def history(self):
        print("You can see the recent videos")

    def ads(self):
        print("Ads will run")

    def quality(self):
        print("Quality is low")

    def access(self):
        print("You have limited access")

    def download(self):
        print("You can't download high-quality videos")


# Premium user
class PremiumHotstar(Hotstar):

    def __init__(self, name):
        print(f"Welcome to Premium Hotstar, {name}")

    # Method overriding
    def ads(self):
        print("Ads will not run")

    def quality(self):
        print("Quality is high")

    def access(self):
        print("You have unlimited access")

    def download(self):
        print("You can download high-quality videos")


# Normal user
a = Hotstar("Chandra")
a.login()
a.dashboard()
a.search()
a.playcontrollers()
a.history()
a.ads()
a.quality()
a.access()
a.download()


print("--------------------")


# Premium user
b = PremiumHotstar("Vaishu")
b.login()
b.dashboard()
b.search()
b.playcontrollers()
b.history()
b.ads()
b.quality()
b.access()
b.download()