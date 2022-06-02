import db


class ClientController:

    def get_client_by_id(selfself, id):
        pass

    def get_all_clients(self):
        for client in db.clients:
            print(client.name)

    def remove_client(self, id):
        pass

    def add_client(self, new_client):
        db.clients.append(new_client)

    def update_client(self):
        pass
