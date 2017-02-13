# Script to send API requests to Google API's
import requests

# Constants
GOOGLE_API_KEY = 'YOUR API KEY'
GOOGLE_TRANSLATE_URL = 'https://translation.googleapis.com/language/translate/v2'

def translate_message(text, target_lang):
    # Package params into dictionary for GET request.
    params = {
        'key':GOOGLE_API_KEY,
        'q': text,
        'source': 'en',
        'target': target_lang
    }

    # Send POST request to Google.
    r = requests.get(GOOGLE_TRANSLATE_URL, params=params)

    # Check if success, if success, return translated text. If not, return error message.
    if r.status_code != 200:
        return 'Something wrong happened, try again later!'

    translated_text = r.json()['data']['translations'][0]['translatedText']
    return translated_text
