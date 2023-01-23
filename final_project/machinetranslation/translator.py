import os
from ibm_watson import LanguageTranslatorV3
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
VERSION_LT = '2018-05-01'
language_translator = LanguageTranslatorV3(version = VERSION_LT, authenticator = authenticator)
language_translator.set_service_url(url)

def english_to_french(english_text):
    '''Translates english to french'''
    french_text = language_translator.translate(english_text, model_id = 'en-fr').get_result()
    return french_text['translations'][0]['translation']
print(english_to_french(input("Please Input English Text: ")))

def french_to_english(french_text):
    ''' Translates french into english.'''
    english_text = language_translator.translate(french_text, model_id = 'fr-en').get_result()
    return english_text['translations'][0]['translation']
print(french_to_english(input("Please Input French Text: ")))
