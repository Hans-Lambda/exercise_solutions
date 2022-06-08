import db
import uuid
import datetime


class User:

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password


class Ticket:

    def __init__(self, price, issued_by):
        self.id = uuid.uuid4()
        self.price = price
        self.issued_by = issued_by


class FlightTicket(Ticket):

    def __init__(self, from_, to, price, issued_by):
        super().__init__(price, issued_by)
        self.from_ = from_
        self.to = to

    def __str__(self):
        return f'{self.from_}-->{self.to}:{self.price}:{self.issued_by}-{self.id}'

    def __repr__(self):
        return f'{self.from_}-->{self.to}:{self.price}:{self.issued_by}-{self.id}'


class EventTicket(Ticket):

    def __init__(self, name, address, price, issued_by):
        super().__init__(price, issued_by)
        self.name = name
        self.address = address


class Token:

    def __init__(self, user):
        self.token = uuid.uuid4()
        self.user = user
        self.issued_on = datetime.datetime.now()
        self.valid_for = 6  # in hours


class UsersController:

    def __init__(self):
        self.list_of_users = self.load_users()

    def get_user(self, username):
        for user in self.list_of_users:
            if user.username == username:
                return user
        raise Exception("User Not Found!")

    def load_users(self):
        list_of_users_obj = []
        for user in db.users:
            new_user = User(user["name"], user["username"], user["password"])
            list_of_users_obj.append(new_user)
        return list_of_users_obj


class Authenticator:

    def __init__(self):
        self.users_tokens = {}
        self.user_controller = UsersController()

    def authenticate(self, username, password):
        user = self.user_controller.get_user(username)
        if user.password == password:
            token = Token(user)
            self.users_tokens[user.username] = token
            return token
        else:
            raise Exception("Authentication Failed!")


class TicketAgent:

    def __init__(self, token):
        self.token = token
        self.flight_tickets = self.load_flight_tickets()
        self.event_tickets = self.load_event_tickets()

    def search_flights(self, from_, to):
        results = []
        for ticket in self.flight_tickets:
            if ticket.from_ == from_ and ticket.to == to:
                results.append(ticket)

        return results

    def search_events(self, event):
        # TOD implement the logic
        # TOD return a list of Events (class)
        return []

    def search_companies(self, search_str):
        # TOD implement the method
        # TOD return a list of companies (class)
        return []

    def load_flight_tickets(self):
        flights = []
        for flight_ticket in db.flight_tickets:
            flight = FlightTicket(flight_ticket["from"], flight_ticket["to"], flight_ticket["price"], flight_ticket["issued_by"])
            flights.append(flight)
        return flights

    def load_event_tickets(self):
        event_tickets = []
        for event_ticket in db.event_tickets:
            ticket = EventTicket(event_ticket["name"], event_ticket["address"], event_ticket["price"], event_ticket["issued_by"])
            event_tickets.append(ticket)
        return event_tickets


class AccountManager:

    def __init__(self, token):
        self.token = token
        self.current_user = None

    def get_user(self, token):
        # TOD implement the logic
        return None


if __name__ == '__main__':

    user = input("Type your username: ")
    password = input("Type your password: ")

    authenticator = Authenticator()
    token = authenticator.authenticate(user, password)
    print(f"Authenticated with Token {token}")

    ticket_agent = TicketAgent(token)
    account_manager = AccountManager(token)

    print("1. Search for flight tickets...")
    print("2. Search for event tickets...")
    print("3. Find companies...")
    print("4. Manage Your Account")
    option = int(input(">>"))

    if option == 1:
        from_ = input("From where? ")
        to = input("To... ")
        list_of_flights = ticket_agent.search_flights(from_, to)
        print(list_of_flights)
    elif option == 2:
        event = input("Type the event name: ")
        list_of_tickets = ticket_agent.search_events(event)
    elif option == 3:
        search_str = input("Type a text to search for companies: ")
        companies = ticket_agent.search_companies(search_str)
    elif option == 4:
        account_manager.current_user.set_name("Mathias")
        user_account = account_manager.get_user(token)
        print(user)
