from os.path import exists
from csv import DictReader, DictWriter

def get_info():
    first_name = input("Введи имя: ")
    last_name = input("Введи фамилию: ")
    phone_number = input("Введи номер телефона: ")

    return [first_name, last_name, phone_number]

def create_file(file_name):
    with open(file_name, "w", encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=["Имя", "Фамилия", "Номер телефона"])
        f_writer.writeheader()

def read_file(file_name):
    with open(file_name, "r", encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)
    
def write_file(file_name, lst):
    res = read_file(file_name)
    obj = {"Имя": lst[0], "Фамилия": lst[1], "Номер телефона": lst[2]}
    res.append(obj)
    with open(file_name, "w", encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=["Имя", "Фамилия", "Номер телефона"])
        f_writer.writeheader()
        f_writer.writerows(res)

def copy_record(source_file, destination_file, row_number):
    source_records = read_file(source_file)
    if row_number < 1 or row_number > len(source_records):
        print("Ошибка: Некорректный номер строки.")
        return
    
    record_to_copy = source_records[row_number - 1]
    
    if not exists(destination_file):
        create_file(destination_file)

    destination_records = read_file(destination_file)
    destination_records.append(record_to_copy)
    
    with open(destination_file, "a", encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=["Имя", "Фамилия", "Номер телефона"])
        f_writer.writeheader()
        f_writer.writerows(destination_records)

file_name = "phone.csv"

def main():
    while True:
        command = input("Введите команду: ")
        if command == 'q':
            break
        elif command == "w":
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == "r":
            if not exists(file_name):
                print("Файл отсуствует. Создайте его")
                continue
            print(*read_file(file_name))
        elif command == "c":
            source_file = input("Введите имя файла-источника: ")
            destination_file = input("Введите имя файла-приемника: ")
            row_number = int(input("Введите номер строки для копирования: "))
            copy_record(source_file, file_name, row_number)

main()