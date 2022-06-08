class OK:

    def __init__(self):

        self.code = 200
        self.message = "OK"


class NotFound:

    def __init__(self):
        self.code = 404
        self.message = "Not Found"


class ServerError:

    def __init__(self):
        self.code = 500
        self.message = "Server Error"

