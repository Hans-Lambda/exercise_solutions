from fastapi import APIRouter
from controller import BikeController, ClientController, PartnerController, BillingController
from db import DataController, bills, partners, clients, bikes
from models import Bike, Client, Partner, Bill


bike_routes = APIRouter()
bike_controller = BikeController()
client_controller = ClientController()
partner_controller = PartnerController()
billing_controller = BillingController()
data_controller = DataController()


# bike routes
@bike_routes.get('/bikes/list_all', tags=['bikes'])
def get_bikes():
    return bike_controller.list_bikes()


@bike_routes.get('/bikes/manufacturer', tags=['bikes'])
def list_bikes_by_manufacturer(manufacturer: str):
    return bike_controller.list_bikes_by_manufacturer(manufacturer)


@bike_routes.get('/bikes/name', tags=['bikes'])
def list_bikes_by_name(name: str):
    return bike_controller.list_bikes_by_name(name)


@bike_routes.post('/bikes/add', tags=['bikes'])
def add_bike(bike: Bike):
    bike_controller.add_bike(bike)
    data_controller.store_bikes()


@bike_routes.delete('/bikes/remove', tags=['bikes'])
def remove_bike(id_: str):
    bike_controller.remove_bike(id_)
    data_controller.store_bikes()


# client routes
@bike_routes.get('/clients/list_all', tags=['clients'])
def list_clients():
    return client_controller.list_clients()


@bike_routes.get('/clients/bill', tags=['clients'])
def list_clients_by_bill(id_: str):
    return client_controller.list_clients_by_bill(id_)


@bike_routes.get('/clients/name', tags=['clients'])
def list_clients_by_name(name: str):
    return client_controller.list_clients_by_name(name)


@bike_routes.post('/clients/add', tags=['clients'])
def add_client(client: Client):
    client_controller.add_client(client)
    data_controller.store_clients()


@bike_routes.patch('/client/modify', tags=['clients'])
def modify_client(email: str):
    client_controller.modify_client(email)
    data_controller.store_clients()


@bike_routes.delete('/clients/remove', tags=['clients'])
def remove_client(email: str):
    client_controller.remove_client(email)
    data_controller.store_clients()


# partner routes
@bike_routes.get('/partners/list_all', tags=['partners'])
def list_partners():
    return partner_controller.list_partners()


@bike_routes.get('/partners/bill', tags=['partners'])
def list_partners_by_bill(id_: str):
    return partner_controller.list_partners_by_bill(id_)


@bike_routes.get('/partners/bike', tags=['partners'])
def list_partners_by_bike(id_: str):
    return partner_controller.list_partners_by_bike(id_)


@bike_routes.get('/partners/name', tags=['partners'])
def list_partners_by_name(name: str):
    return partner_controller.list_partners_by_name(name)


@bike_routes.post('/partners/add', tags=['partners'])
def add_partner(partner: Partner):
    partner_controller.add_partner(partner)
    data_controller.store_partners()


@bike_routes.patch('/partners/modify', tags=['partners'])
def modify_partner(email: str):
    partner_controller.modify_partner(email)
    data_controller.store_partners()


@bike_routes.delete('/partners/remove', tags=['partners'])
def remove_partner(email: str):
    partner_controller.remove_partner(email)
    data_controller.store_partners()


# bill routes
@bike_routes.get('/bills/list_all', tags=['bills'])
def get_bills():
    return billing_controller.get_bills()


@bike_routes.get('/bills/open', tags=['bills'])
def get_open_bills():
    return billing_controller.get_open_bills()


@bike_routes.get('/bills/closed', tags=['bills'])
def get_closed_bills():
    return billing_controller.get_closed_bills()


@bike_routes.get('/bills/id', tags=['bills'])
def get_bill_by_id(id_: str):
    return billing_controller.get_bill_by_id(id_)


@bike_routes.get('/bills/bike', tags=['bills'])
def get_bills_by_bike(id_: str):
    return billing_controller.get_bills_by_bike(id_)


@bike_routes.get('/bills/partner', tags=['bills'])
def get_bills_by_partner(email: str):
    return billing_controller.get_bills_by_partner(email)


@bike_routes.get('/bills/client', tags=['bills'])
def get_bills_by_client(email: str):
    return billing_controller.get_bills_by_client(email)


@bike_routes.post('/bills/new', tags=['bills'])
def new_bill(client, bike, billing_method, billing):
    billing_controller.new_bill(client, bike, billing_method, billing)
    data_controller.store_bills()
