from translate import Translator

while True:
    try:
        lang = input("Enter the language you want to translate into: ")
        text = input("Enter the text you want to translate: ")

        translator = Translator(to_lang=lang)
        translation = translator.translate(text)
        print(translation)
    except KeyboardInterrupt:
        break
