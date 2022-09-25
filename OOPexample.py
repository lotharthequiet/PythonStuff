#!/bin/python3


class Car:

    DealershipName = "Leone's Automart"

    def __init__(self,carmake,carmodel,caryear,carcolor,trimlevel,carmiles):
        self.make = carmake
        self.model = carmodel
        self.year = caryear
        self.color = carcolor
        self.trim = trimlevel
        self.miles = carmiles

    def get_make(self):
        return self.make

    def set_make(self, make):
        self.make = make

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_color(self):
        return self.color

    def set_color(self, carcolor):
        self.color = carcolor

    def get_trim(self):
        return self.trim
    
    def set_trim(self, trimlevel):
        self.trim = trimlevel
    
    def get_miles(self):
        return self.miles

    def set_miles(self, miles):
        self.miles = miles

    def get_info(self):
        return self.year, self.make, self.model, self.color, self.trim, self.miles

    def inv_list():
        print(Car.DealershipName)
        print("Inventory Report:")
        print(c1.get_year(), c1.get_make(), c1.get_model(), c1.get_color(), c1.get_trim(), c1.get_miles())
        print(c2.get_year(), c2.get_make(), c2.get_model(), c2.get_color(), c2.get_trim(), c2.get_miles())
        print(c3.get_year(), c3.get_make(), c3.get_model(), c3.get_color(), c3.get_trim(), c3.get_miles())
        print(c4.get_year(), c4.get_make(), c4.get_model(), c4.get_color(), c4.get_trim(), c4.get_miles())
        print(c5.get_year(), c5.get_make(), c5.get_model(), c5.get_color(), c5.get_trim(), c5.get_miles())
        print(c6.get_year(), c6.get_make(), c6.get_model(), c6.get_color(), c6.get_trim(), c6.get_miles())


c1 = Car("Ford", "Ranger", "1987", "Black", "N/A", "87,000")
c2 = Car("Buick", "Regal", "1995", "White", "GS", "112,500")
c3 = Car("Chevrolet", "S-10", "1997", "Silver", "LS", "95,000")
c4 = Car("Lexus", "GS-430", "2003", "Silver", "N/A", "120,000")
c5 = Car("BMW", "328i", "2012", "White", "N/A", "65,000")
c6 = Car("Toyota", "4Runner", "2016", "Pearl", "Limited", "85,000")

Car.inv_list()

print(c1.get_info())
