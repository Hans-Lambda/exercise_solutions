from channels import ChannelManager


class App:

    def __init__(self):

        self.name = None
        self.number = None
        self.email = None
        self.password = None


# TDo  * restructure dict to list of dict
#       * then first make app object, afterwards verification


class AppManager:

    def __init__(self):

        self.data = {"Netflix": {"Email": "netflix@email.com", "Password": "netflixpw"},
                     "Amazon Prime": {"Email": "amazon@email.com", "Password": "amazonpw"}}
        self.apps = []
        apple = App()

    def verification(self, app):
        print(f"Please provide your {app} email-address and password")
        email = input("Please enter your email address: ")
        password = input("Please enter your password: ")
        return app["Email"] == email and app["Password"] == password

    def add_app(self):

        choice = -1
        while choice != "0":
            print(f"Do you want to use any of the following apps?\n0. Exit")
            [print(f"{count + 1}. {app}") for count, app in enumerate(self.data)]
            choice = input("Enter your choice")
            for app in self.data:
                if choice == "1":
                    if self.verification(self.data[app]):
                        number = input(f"Please enter desired channel number for {self.data[app]}")
                        self.edit_channel(self.data[app], number)
                if choice == "2":
                    if self.verification(self.data[app]):
                        number = input(f"Please enter desired channel number for {self.data[app]}")
                        self.edit_channel(self.data[app], number)
