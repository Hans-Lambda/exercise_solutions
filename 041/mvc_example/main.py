from view import ClientView, MainView
from controllers import ClientController


if __name__ == '__main__':

    client_controller = ClientController()
    client_view = ClientView(client_controller)
    main_view = MainView(client_view)

    main_view.main_menu()
