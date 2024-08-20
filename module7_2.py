from pprint import pprint

def custom_write(file_name, string):
    string_position = {}
    n = 0
    file = open(file_name, 'a', encoding= 'utf-8')
    for i in string:
        b_nr = file.tell()
        file.write(i + '\n')
        n += 1
        string_position.update({(n, b_nr): i})
    return string_position

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)


