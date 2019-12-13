from googletrans import Translator

class SerialTranslator:

    def __init__(self):
        self.text = ""
        self.language_dict = self.load_languages()
        self.langlist = []
        self.translator = Translator()

    @staticmethod
    def load_languages():
        input_dict = {'German': "de",
                      'Croatian': 'hr',
                      'Belarusian': 'be',
                      'Bulgarian': 'bg',
                      'Macedonian': 'mk',
                      'Russian': 'ru',
                      'Serbian': 'sr',
                      'Slovenian': 'sl',
                      'English': 'en',
                      'Spanish': 'es',
                      'Portuguese': 'pt'
                         }
        return input_dict

    def translate(self, text, in_lang_code, out_lang_code):
        return self.translator.translate(text, src=in_lang_code, dest=out_lang_code).text

    @staticmethod
    def get_input():
        text = input('Please enter Text to translate: \n')
        return text


    def serial_translation(self, text, in_language, language_list):
        #appending input language at beginning and
        translate_list = []
        translate_list.append(in_language)
        for lang in language_list:
            translate_list.append(lang)
        translate_list.append(in_language)

        for lang_index in range(len(translate_list)-1):
            print(f'Translating from {translate_list[lang_index]} to {translate_list[lang_index+1]}')
            in_code = self.get_lang_code(translate_list[lang_index])
            out_code = self.get_lang_code(translate_list[lang_index+1])
            #print(f'Incode: {in_code} Outcode {out_code}')
            text = self.translate(text, in_code, out_code)

        return text

    def get_language_options(self):
        return list(self.language_dict.keys())


    def get_lang_code(self, lang):
        return self.language_dict[lang]

def test():
    testtrans = SerialTranslator()
    #text = SerialTranslator.get_input()
    text = "Oh Tannenbaum, oh Tannenbaum, wie grün sind deine Blätter. Du grünst nicht nur zur Sommerszeit, nein auch im Winter, wenn es schneit."
    funtrans = testtrans.serial_translation(text, 'German', ['English', 'Bulgarian', 'Croatian', 'Belarusian','Slovenian','Serbian','Macedonian'])
    print(funtrans)
#test()
