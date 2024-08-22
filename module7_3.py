class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, 'r', encoding= 'utf-8') as file:
                info = file.read().lower()
                for sym in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    info = info.replace(sym, '')
                    all_words[name] = info.split()
        return all_words

    def find(self, word):
        word = word.lower()
        search_result = {}
        for name, words in self.get_all_words().items():
            word_index = words.index(word) + 1
            search_result.update({name: word_index})
        return search_result

    def count(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            word_count = 0
            for i in words:
                if i == word.lower():
                    word_count += 1
                    result.update({name: word_count})
        return result



finder2 = WordsFinder('test_file.txt', 'test_file_2.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))