"""
translates texts from english to french and french to english
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
    )

language_translator.set_service_url(
    'https://api.us-east.language-translator.watson.cloud.ibm.com/instances/52758114-3b71-433c-8006-ea65f0d26b3f')

def englishToFrench(English_Text):
    """
    funtion that translates english text to french text and returns french text
    """
    french_text = language_translator.translate(text=English_Text,
    model_id='en-fr').get_result()
    return french_text.get("translations")[0].get("translate")

def frenchToEnglish(French_Text):
    """
    translates french text to english text
    """
    english_text = language_translator.translate(text=(French_Text),
    model_id='en-fr').get_result()
    return english_text.get("translations")[0].get("translate")
