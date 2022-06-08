from abc import ABC, abstractmethod


class Sender(ABC):

    def __init__(self):
        self.status = "Ok"

    @abstractmethod
    def send(self, message):
        pass

    def sender_status(self):
        print(f'Sender Status is: {self.status}')


class PlainTextSender(Sender):

    def send(self, message):
        print(f"Message Sent! >>> {message}")


class EncryptedSender(Sender):

    def send(self, message):
        # This is not a real encryption...
        enc_message = str()
        for char in message:
            enc_message += 'A'

        print(f"Message Sent {enc_message}")


class ReverseSender(Sender):

    def send(self, message):
        # another approach to reverse the string ---> rstring = ''.join(reversed(string))
        print(f"Message Sent {message[::-1]}")


class Chat:

    def __init__(self, sender: Sender):
        if not isinstance(sender, Sender):
            raise Exception("Cannot proceed invalid Sender object...")
        self.sender = sender
        sender.sender_status()

    def send_message(self, message):
        self.sender.send(message)


if __name__ == '__main__':

    sender_obj = PlainTextSender()
    chat = Chat(sender_obj)
    chat.send_message("Hi Mathias...")

    enc_sender = EncryptedSender()
    chat = Chat(enc_sender)
    chat.send_message("Hi Mathias...")

    rev_sender = ReverseSender()
    chat = Chat(rev_sender)
    chat.send_message("Hi Mathias...")

    # broken_sender = "This is not a sender, this is a string"
    # chat = Chat(broken_sender)
    # chat.send_message("Hi Mathias...")

