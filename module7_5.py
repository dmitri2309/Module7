import os
import time

print(os.getcwd())
for root, dirs, files in os.walk('.'):
    for file in files:
        if file == 'Product.txt':
            file_path = os.path.join(os.getcwd(), file)
            filetime = os.path.getmtime(file)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            file_size = os.path.getsize(file)
            parent_dir = os.path.dirname(file_path)
            print(f'Обнаружен файл: {file}, Путь: {file_path}, Размер: {file_size} байт,\nВремя изменения: {formatted_time},'
                  f'Родительская директория: {parent_dir}')