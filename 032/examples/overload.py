# overloading means let a method behave in another way

# make the same method but provide it with more arguments, python will decide which to use


class Ticket:

    # def findTicket(self, name, maximum=None , minimum=None):
    #     if maximum == None and minimum == None:
    #         print(f"Ola {name}")
    #     elif maximum is not None and minimum is None:
    #         print(f"Ola {name} -> Maximum {maximum}")

    def findTicket(self, name, **kwargs):
        print(kwargs["maximum"])
        print(kwargs["minimum"])
        print(kwargs["avg"])


if __name__ == '__main__':

    t = Ticket()
    #t.findTicket("Mathias", 1000)
    t.findTicket("Mathias", maximum=1000, minimum=0, avg=500)

