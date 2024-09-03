from translate import Translator


def main() -> None:
    """Main code"""
    while True:
        try:
            lang = input("Enter the language you want to translate into: ")
            text = input("Enter the text you want to translate: ")

            translator = Translator(to_lang=lang)
            translation: str = str(translator.translate(text))
            print(translation)
        except KeyboardInterrupt:
            break
