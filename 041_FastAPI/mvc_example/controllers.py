import uuid

import db


class ClientController:

    def get_client_by_id(self, id):
        pass

    def get_all_clients(self):
        for client in db.clients:
            print(client.name)

    def remove_client(self, id):
        pass

    def add_client(self, new_client):
        db.clients.append(new_client)

    def update_client(self, id, new_data):
        pass


class PartnerController:

    def get_partner_by_id(self, id):
        pass


class BillController:

    def add_new_bill(self, bill):
        pass


class BikeController:

    def add_new_bike(self, bike):
        pass
