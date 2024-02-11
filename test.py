import os

def print_menu():
    '''Функция для вывода меню'''
    print("Телефонный справочник")
    print("1. Вывести все записи")
    print("2. Добавить новую запись")
    print("3. Редактировать запись")
    print("4. Поиск записей")
    print("5. Выход")


def read_contacts():
    '''Функция для чтения данных из файла'''
    contacts = []
    if os.path.exists("contacts.txt"):
        with open("contacts.txt", "r", 'utf-8') as file:
            for line in file:
                contacts.append(line.strip().split(','))
    return contacts

def write_contacts(contacts):
    '''Функция для записи данных в файл'''
    with open("contacts.txt", "w", 'utf-8') as file:
        for contact in contacts:
            file.write(','.join(contact) + '\n')


def print_contacts(contacts, page, page_size):
    '''Функция для вывода записей постранично'''
    start_index = (page - 1) * page_size
    end_index = min(start_index + page_size, len(contacts))
    for i in range(start_index, end_index):
        print(f"{i+1}. {' | '.join(contacts[i])}")


def add_contact(contacts):
    ''' Функция для добавления новой записи'''
    new_contact = []
    print("Введите данные новой записи:")
    new_contact.append(input("Фамилия: "))
    new_contact.append(input("Имя: "))
    new_contact.append(input("Отчество: "))
    new_contact.append(input("Название организации: "))
    new_contact.append(input("Рабочий телефон: "))
    new_contact.append(input("Личный телефон: "))
    contacts.append(new_contact)
    write_contacts(contacts)
    print("Запись успешно добавлена.")


def edit_contact(contacts):
    '''Функция для редактирования записи'''
    print("Введите номер записи, которую хотите отредактировать:")
    index = int(input()) - 1
    if index >= 0 and index < len(contacts):
        print("Введите новые данные для записи:")
        contacts[index][0] = input("Фамилия: ")
        contacts[index][1] = input("Имя: ")
        contacts[index][2] = input("Отчество: ")
        contacts[index][3] = input("Название организации: ")
        contacts[index][4] = input("Рабочий телефон: ")
        contacts[index][5] = input("Личный телефон: ")
        write_contacts(contacts)
        print("Запись успешно отредактирована.")
    else:
        print("Некорректный номер записи.")

def search_contacts(contacts):
    '''Функция для поиска записей'''
    print("Введите характеристики для поиска (разделите пробелом):")
    query = input().split()
    results = []
    for contact in contacts:
        if all(term.lower() in ' '.join(contact).lower() for term in query):
            results.append(contact)
    if results:
        print("Найденные записи:")
        for i, result in enumerate(results):
            print(f"{i+1}. {' | '.join(result)}")
    else:
        print("Записи не найдены.")

def main():
    contacts = read_contacts()
    page_size = 5
    page = 1
    while True:
        print_menu()
        choice = input("Выберите действие: ")
        if choice == '1':
            print_contacts(contacts, page, page_size)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            search_contacts(contacts)
        elif choice == '5':
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие из списка.")
        input("Нажмите Enter для продолжения...")
        os.system('cls' if os.name == 'nt' else 'clear')  # Очистка экрана

if __name__ == "__main__":
    main()
