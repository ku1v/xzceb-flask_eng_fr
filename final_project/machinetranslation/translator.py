import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

VERSION = '2023-03-29'
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(english_text):
    '''
    This function accepts the English text string us input  
    and returns the French text string as output
    '''
    try: 
        french_text = language_translator.translate(
                       text=english_text,
                       model_id='en-fr').get_result()
        return french_text['translations'][0]['translation']
    except:
        return None


def frenchToEnglish(french_text):
    '''
    This function accepts the Franche text string us input  
    and returns the English text string as output
    '''
    try:
        english_text = language_translator.translate(
                       text=french_text,
                       model_id='fr-en').get_result()
        return english_text['translations'][0]['translation']
    except:
        return None
