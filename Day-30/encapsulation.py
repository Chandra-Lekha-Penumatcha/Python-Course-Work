class Instagram:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
        self._posts = []

    def getpassword(self):
        return self.__password

    def setpassword(self, newpassword):
        self.__password = newpassword

    @property
    def accesspost(self):
        return self._posts

    @accesspost.setter
    def accesspost(self, newpost):
        self._posts.append(newpost)

    def display(self):
        print(self.username, self.__password, self._posts)


chandra = Instagram('chandra', 'chandra@123')

chandra.display()
print(chandra.username)
print(chandra.getpassword())
print(chandra.accesspost)

chandra.username = 'chandra'
chandra.setpassword("chandra@123")

chandra.accesspost = "sunrise.png"
chandra.accesspost = "beach.png"
chandra.accesspost = "mountains.png"

print(chandra.username)
print(chandra.getpassword())
print(chandra.accesspost)