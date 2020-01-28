from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_directory
import sys
from human_ft_computer_game_1 import game
try:
    command = sys.argv[1]
except IndexError:
    print('Необходимо выбрать команду')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла или папки')
        else:
            delete_file(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            try:
                new_name = sys.argv[3]
            except IndexError:
                print('Отсутстует название копии файла или папки')
            else:
                copy_file(name, new_name)
        except IndexError:
            print('Отсутствует название копируемого(-ой) файла или папки')
    elif command == 'change_directory':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название измененной текущей директории')
        else:
            change_directory(name)
    elif command == 'help':
        print('list - список файлов и папок')
        print('create_file - создание файла')
        print('create_folder - создание папки')
        print('delete - удаление файла или папки')
        print('copy - копирование файла или папки')
    elif command == 'game':
        game()





