from google.cloud import translate_v2 as translate
import six
import os
import json

config_file = open("config.json", "r")
config = json.load(config_file)
credential_path = config["credential_path"]
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

translate_client = translate.Client()

def translate_text(target, text):
    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')
    result = translate_client.translate(text, target_language=target)
    return result['translatedText']