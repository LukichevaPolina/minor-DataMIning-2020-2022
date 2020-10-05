import os
path = 'C:\\Users\\Polina\\Documents\\test'
for dirpath, dirnames, filenames in os.walk(path):
    # перебрать каталоги
    for dirname in dirnames:
        print("Каталог:", os.path.join(dirpath, dirname))
    # перебрать файлы
    for filename in filenames:
        print("Файл:", os.path.join(dirpath, filename))