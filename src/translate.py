from google.cloud import translate_v2 as translate
import six
import os
from dotenv import load_dotenv

load_dotenv()
file_path = os.getenv("CREDENTIAL_PATH")
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.abspath(file_path)
translate_client = translate.Client()


def translate_text(target, text):
    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')
    result = translate_client.translate(text, target_language=target)
    return result['translatedText']
