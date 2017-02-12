# Flask application script
from flask import Flask, request, jsonify, Response, render_template
import os
import bot

application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hello World! Nothing is broken... yet!'

@application.route('/webhook', methods=['GET', 'POST'])
def webhook():
    try:
        if request.method == 'GET':
            # Webhook is verified with Facebook Messenger https://developers.facebook.com/docs/graph-api/webhooks
            if request.args.get('hub.verify_token') == '12345':
                return Response(request.args.get('hub.challenge'))
            else:
                return Response('Wrong validation token.')
        else:
            # Here messages in a form of JSON are received, code for this is handled in bot.py
            return bot.response_handler(request.get_json())
    except:
        return Response('Application error.')

if __name__ == '__main__':
    application.debug = True
    port = int(os.environ.get("PORT", 5000))
    application.run(host='0.0.0.0',port = port, debug = True)
