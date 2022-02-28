class Person:
    def __init__(self, name, addr, ph):
        self.__name = name
        self.__addr = addr
        self.__phone = ph

    def print_person(self):
        print("Name:", self.__name)
        print("Address:", self.__addr)
        print("Phone:", self.__phone)


class Customer(Person):
    def __init__(self, name, addr, ph, cnum, ml):
        Person.__init__(self, name, addr, ph)

        self.__cnum = cnum
        self.__mail_list = ml

    def print_person(self):
        Person.print_person(self)
        print("Customer Number:", self.__cnum)
        print("Wants to be on Mailing List?", self.__mail_list)
