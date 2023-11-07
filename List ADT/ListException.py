class ListException(Exception):
    def __init__(self, message = "An Unknow Error Occurs!"):
        print(message)