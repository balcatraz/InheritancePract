import PersonClass as p


def main():
    person = p.Person("Bob", "123 Street Waco TX", "210-212-2121")
    person.print_person()

    customr = p.Customer("Frank", "124 Street Waco TX", "254-232-3456", 1, False)
    customr.print_person()


main()
