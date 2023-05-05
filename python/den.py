import string

class TextProcessor:
    def __init__(self):
        self.__ind = None

    def __is_punctuation(self, char):
        if char in string.punctuation:
            self.__ind = True
            return self.__ind
        else:
            self.__ind = False
            return self.__ind

    def access_punctuation(self, char):
        self.__is_punctuation(char)

    def get_clean_string(self, old_string):
        for char in old_string:
            self.access_punctuation(char)
            if self.__ind:
                old_string = old_string.replace(char, '')
        return old_string


class TextLoader:
    def __init__(self, text_processor):
        if not isinstance(text_processor, TextProcessor):
            raise TypeError('Argument should be instance of TextProcessor class.')
        self.__text_processor = text_processor
        self.__clean_string = None

    def set_clean_text(self, old_string):
        self.__clean_string = self.__text_processor.get_clean_string(old_string)
        return self.__clean_string


class DataInterface:

    def __init__(self, text_loader):
        if not isinstance(text_loader, TextLoader):
            raise TypeError('Argument should be instance of TextLoader class.')
        self._text_loader = text_loader

    def process_texts(self, unprocessed_text):
        processed_text = []
        for elem in unprocessed_text:
            processed_text.append(self._text_loader.set_clean_text(elem))
        return processed_text

my_str = TextProcessor()
print(my_str.get_clean_string("Why ,are ,we ,still ,here!?"))
my_str2 = TextLoader(my_str)
print(my_str2.set_clean_text("Why ,are ,we ,still ,here!?"))
my_str3 = DataInterface(my_str2)
print(my_str3.process_texts(["j,u.s!t", ":t;o", "s;u!f;f?e@r$"]))