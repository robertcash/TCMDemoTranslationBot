# Script to send messages to FB Messenger via FB Messenger Send API
import requests

# Constants
FB_ACCESS_TOKEN = 'EAAI3PTX0WzgBAAU4sksCWvwRNrTqX5DtdeRpnVt668KW6kui9TDIAs1grGbQwxuAxTtaiss7Gey76iDm9zZCyZBn93wUyhB5v1iYVBqAVOb5kewtFRBJODXgvaAc4ydZADlEuqgEpndwubIMG5eFjZBFUk1srEownIZCiqSHlZAwZDZD'
SEND_API_URL = 'https://graph.facebook.com/v2.6/me/messages?access_token=' + FB_ACCESS_TOKEN

def send_message(messenger_id, text):
    # Package params into dictionaries for POST request
    recipient = {'id':messenger_id}
    message = {'text':text}
    params = {'recipient':recipient, 'message':message}

    # Send POST request to Facebook Messenger Send API to send text message
    r = requests.post(SEND_API_URL, json=params)
