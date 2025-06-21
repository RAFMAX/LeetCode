class Person:
    def __init__(self, name, country, date):
        self.name = name
        self.country = country
        self.date = date
    def find_age(self):
        return (2025 - int(self.date))
    
name = input("Give Name : ")
country = input("Give Country : ")
date = input("Give Date Of Birth : ".title())
Guy = Person(name, country, date)
print(Guy.find_age())