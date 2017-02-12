# Script that houses main logic of bot
from messenger_parser import MessengerParser
from google_api_requests import translate_message
from messenger_api_requests import send_message
from helpers import response

# Constants
TARGET_LANGUAGE = 'pt' # For other language codes: https://cloud.google.com/translate/docs/languages

def response_handler(request):
    # Grabs JSON request and makes it MessengerParser object for easy use
    received_message = MessengerParser(request)

    # Uses translate_message function in google_api_requests.py to translate user message
    translation = translate_message(received_message.text, TARGET_LANGUAGE)

    # Uses send_message function in messenger_parser.py to send translated message back to user
    send_message(received_message.messenger_id, translation)

    # Ends FB's webhook request with a response with a 200 success code
    return response()
