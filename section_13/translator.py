from pycountry import languages
from translate import Translator

while True:
    language = input(
        'Which language should we translate to? (ISO 639-1 two letter code, e.g. "uk")? '
    )
    try:
        languages.lookup(language)
        break
    except LookupError:
        print(f"language {language} is not valid, please try again")

translator = Translator(to_lang=language)

try:
    with open("./translate.txt", mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
except FileNotFoundError:
    print("File not found!")

outfile = f'./out-{language}.txt'
with open(outfile, mode='w') as my_file:
    my_file.write(translation)
