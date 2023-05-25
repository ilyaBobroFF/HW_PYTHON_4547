def create(data):
    try:
        file = open(data, 'r')
    except IOError:
        print(f"Создан новый справочник -> {data}")
        file = open(data, 'w')
    finally:
        file.close()

def add_name(file_name, entry):
    data = open(file_name, 'a')
    data.write(entry + "\n")
    data.close()
    print("Новый контакт добавлен \n")
    

def show_all(file_name):
    data = open(file_name, "r")
    for line in data:
        print(line[:-1])
    data.close()
    print("Список контактов завершен \n")


def search(file_name, s_name):
    not_name = True
    data = open(file_name, 'r')
    for line in data:
        if s_name in line:
            print(line[:-1] + "\nПоиск завершен")
            not_name = False
    if not_name: print("Контакт не найден")
    data.close()

def del_name(file_name, del_name):
    data = open(file_name, 'r')
    list_name = list()
    for line in data:
        if del_name in line: 
            print_name = line
            continue
        if line != "": list_name.append(line)
    data.close()
    list_name = list(filter(lambda x: x !="", list_name))
    data = open(file_name, 'w')
    for item in list_name:
        data.write(item)
    data.close()
    print(f"Контакт: {print_name}>>удален<<\n")

def change_name(file_name, ch_name):
    data = open(file_name, 'r')
    list_name = list()
    for line in data:
        if ch_name in line: 
            new_name = input("Введите новое ФИО и номер телефона: ")
            list_name.append(new_name + "\n")
            continue
        list_name.append(line)
    data.close()
    list_name = list(filter(lambda x: x !="", list_name))
    data = open(file_name, 'w')
    for item in list_name:
        data.write(item)
    data.close()
    print()
