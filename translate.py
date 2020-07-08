from google.cloud import translate_v2 as translate
import six
import os

credential_path = r"PATH TO GOOGLE CLOUD CREDENTIAL FILE"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

translate_client = translate.Client()

# def list_languages():
#     results = translate_client.get_languages()
#     for language in results:
#         print(u'{name} ({language})'.format(**language))

def translate_text(target, text):
    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')
    result = translate_client.translate(text, target_language=target)
    return result['translatedText']