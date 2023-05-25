import Function
import Interface
notebook = "phone.txt"
Function.create(notebook)
mode = -1
while mode != 00:
    mode = Interface.main_menu()
    if mode == 1:
        record = Interface.input_str("\nВведите ФИО и номер телефона через пробел: ")
        Function.add_name(notebook, record)
    elif mode == 2:
        print(Function.show_all(notebook))
    elif mode == 3:
        search_name = Interface.input_str("\nВведите Фамилию или Имя для поиска: ")
        Function.search(notebook, search_name)
    elif mode == 4:
        delete_name = Interface.input_str("\nВведите Фамилию или Имя для удаления: ")
        Function.del_name(notebook, delete_name)
    elif mode == 5:
        change_name = Interface.input_str("\nВведите Фамилию или Имя для изменения: ")
        Function.change_name(notebook, change_name)    
print("Выполнен выход")