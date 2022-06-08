class Ticket:

    def find_ticket_multiple_args(self, name, **kwargs):
        print(kwargs['maximum'])
        print(kwargs['minimum'])
        print(kwargs['avg'])


if __name__ == '__main__':
    t = Ticket()
    t.find_ticket("Mathias", maximum=1000, minimum=0, avg=500)
