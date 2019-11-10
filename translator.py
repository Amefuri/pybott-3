from yandex.Translater import Translater
from fuzzywuzzy import process

tr = Translater()
tr.set_key('trnsl.1.1.20191110T032816Z.3c6d2a8836612f9b.6f0e28aa49051c2e8befeb7f1e242d0894a00027') # Api key found on https://translate.yandex.com/developers/keys
    
def translate(from_lang, to_lang, text_from_user):
    tr.set_from_lang(from_lang)
    tr.set_to_lang(to_lang)
    tr.set_text(text_from_user)
    return tr.translate()


corpus = {
    'th' : ['thai', 'ไทย'],
    'fr' : ['france', 'ฝรั่งเศส'],
    'de' : ['getman', 'deutsch', 'เยอรมันนี'],
    'en' : ['english', 'อังกฤษ', 'อิ้ง']
}

while True:
    from_translator = input("choose translator from: ")
    from_translator = process.extractOne(from_translator, corpus)[2]
    print(from_translator)

    to_translator = input("choose translator to: ")
    to_translator = process.extractOne(to_translator, corpus)[2]
    print(to_translator)

    text_from_user = input('Input Text: ')
    translated_text = translate(from_translator, to_translator, text_from_user)
    print('Translated Text: ', translated_text)

    is_retry = input('ต้องการแปลอีกไหมคะ?(Y/N)')
    if is_retry.upper() == 'N':
        break
    


# language_choices = ["th_en", "th_de", "th_fr"]
# selected_language = input('Select Language(th_en, th_de, th_fr): ')
# selected_language = process.extractOne(selected_language, language_choices)[0]


# text_from_user = input('Input Text: ')
# translated_text = ''
# if selected_language == 'th_en':
#     translated_text = translate('th', 'en', text_from_user)
# elif selected_language == 'th_de':
#     translated_text = translate('th', 'de', text_from_user)
# elif selected_language == 'th_fr':
#     translated_text = translate('th', 'fr', text_from_user)

# print('Translated Text: ', translated_text)




# class BotTranslator():

