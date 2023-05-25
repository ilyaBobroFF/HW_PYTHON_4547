def main_menu():
    print("Выберите действие:")          
    print("1 - Добавить новый контакт")
    print("2 - Просмотр всех контактов") 
    print("3 - Найти контакт по Фамилии или Имени")
    print("4 - !УДАЛИТЬ! контакт по Фамилии или Имени")
    print("5 - Изменить введенный контакт")
    print("00 - Для выхода")
    enter = int(input("Введите желаемый вариант работы: "))
    return enter

def input_str(descrip = "Ваш ввод: "):
    in_str = input(descrip)
    return in_str