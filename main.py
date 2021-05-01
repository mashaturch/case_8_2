"""Case-study #8.2 Text generator
Разработчики:
Турчинович М. (), Зубарева Т. () , Костылев М. ()
"""
import os

#можно сделать отдельный файл с оодержанием всяких переменных

MENU = '1. Просмотр каталога\n2. На уровень вверх\n3. На уровень вниз\n' \
       '4. Количество файлов и каталогов\n5. Размер текущего каталога (в байтах)\n' \
       '6. В поисках файла\n7. Выход из программы\nВыберите пункт меню:'
QUIT = 'EXIT'

def main():
    """Calls the rest of the functions"""
    while True:
       print (os.getcwd())
       print (MENU)
       command = acceptCommand()
       if command == QUIT:
          print ('Работа программы завершена.')
          break
       runCommand(command)

def acceptCommand():
    """Checks the correctness of the entered number"""
    number = int (input ())
    if number == 7:
        return 'EXIT'
    if number in [1, 2, 3, 4, 5, 6]:
        return number
    else:
        print ('Ошибка! Выберите пункт меню снова:')
        acceptCommand()

def runCommand(command):


if __name__ == '__main__':
    main()