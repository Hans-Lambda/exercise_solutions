from server_errors import OK, NotFound, ServerError

# https://www.geeksforgeeks.org/polymorphism-in-python/

# Write code to test your classes

def status(error_object):

    print(f"{error_object.message} code error {error_object.code}")
    return f"{error_object.message} code error {error_object.code}"




if __name__ == '__main__':

    ok = OK()
    not_found = NotFound()
    server_errors = ServerError()

    status(ok)
    status(not_found)
    status(server_errors)
