# Class to parse JSON request from FB server

class MessengerParser:
    # Initializer for class, what needs to be called when creating MessengerParser object
    def __init__(self, request):
        # Grab first message in list of messages in JSON request
        message_body = request['entry'][0]['messaging'][0]

        # Grab sender messenger id to keep track of who sent the message
        self.messenger_id = message_body['sender']['id']

        # Grab message and get text out of JSON
        message = request['message']
        self.text = message['text']
