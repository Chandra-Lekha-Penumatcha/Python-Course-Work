class Flipkart:
    products = {'shirts': 10000, 'handbag': 2000, 'pants': 3000}
    discount = 30

    @classmethod
    def display(cls):
        print(cls.products)

    def userinfo(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address
        print(f"Hello {self.name}, Welcome to Flipkart")

    @staticmethod
    def displaydiscount():
        print(f"{Flipkart.discount}% discount is going on, grab the products")


chandra = Flipkart()
chandra.userinfo('chandra', '987654321', 'Hyd')
chandra.displaydiscount()
chandra.display()

vaishu = Flipkart()
vaishu.userinfo('vaishu', '987654321', 'Chennai')
vaishu.displaydiscount()
vaishu.display()


gayathri = Flipkart()
gayathri.userinfo('gayathri','987654321','karntaka')
gayathri.displaydiscount()
gayathri.display

suhi = Flipkart()
suhi.userinfo('suhi', '987654321', 'Bangalore')
suhi.displaydiscount()
suhi.display

Flipkart.displaydiscount()
Flipkart.display()
print(Flipkart.products)

#using object -> ins,cls,sta,clsatt,insatt
#using class -> cls, sta, clsatt
#constructor is instance method because object is called from the class
#constructor is special method that is automatically called when an object is created

