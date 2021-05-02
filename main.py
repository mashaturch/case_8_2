"""Case-study #8_2
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

def moveUp():
    """Moving to a higher level"""
    os.chdir('..')

def moveDown(currentDir):
    """Moving to a level below"""
    if os.path.isdir(currentDir):
        os.chdir(currentDir)
    else:
        currentDir = input('Ошибка! Введите новый каталог снова: ')
        moveDown(currentDir)


def countFiles(path):
    """Counting the number of files"""
    quantity = 0
    for name in os.listdir(path):
        if os.path.isdir(os.path.join(path, name)):
            quantity += countFiles(os.path.join(path, name))
        if os.path.isfile(os.path.join(path, name)):
            quantity += 1
    return quantity

def count_fold_files(path):
    """Counting the number of folders and files"""
    quantity = 0
    for name in os.listdir(path):
        if os.path.isdir(os.path.join(path, name)):
            quantity += countFiles(os.path.join(path, name))
        quantity += 1
    return quantity

def countBytes(path):
    """Counting the total size (in bytes) of all files"""
    quantity_bytes = 0
    for name in os.listdir(path):
        if os.path.isdir(os.path.join(path, name)):
            quantity_bytes += countFiles(os.path.join(path, name))
        if os.path.isfile(os.path.join(path, name)):
            quantity_bytes += os.path.getsize(os.path.join(path, name))
    return quantity_bytes

def runCommand(command):
    """Determination of the required function by the command number"""
    path = os.getcwd()
    print()

    if command == 1:
        for numbers, folders, files in os.walk(path):
            print ('Папки: ', end='')
            for folder in folders:
                print (folder, end='  ')
            print()
            print('Файлы: ', end='')
            for file in files:
                print(file, end='  ')
            print()
            break

    if command == 2:
        moveUp()

    if command == 3:
        currentDir = input('Введите нужный новый каталог: ')
        moveDown(currentDir)

    if command == 4:
        print('Количество файлов:', countFiles(path))
        print('Количество каталогов:', count_fold_files(path) - countFiles(path))

    if command == 5:
        print ('Суммарный объем (в байтах) всех файлов:', countBytes(path))



    print()

if __name__ == '__main__':
    main()