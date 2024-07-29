from src.utils import get_transactions_info, read_excel_file, read_csv_file
from src.processing import filter_by_state, sort_by_date
import os

ROOT_PATH = os.path.dirname(__file__)

# приветствие и выбор формата файла для работы с транзакциями
print('''Привет! Добро пожаловать в программу работы с банковскими транзакциями!

Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n''')

# проверка корректности ввода пользователя
while True:
    try:
        select_file_format = int(input("Введите цифру: "))
    except ValueError:
        print("Некорректный ввод! Пожалуйста, введите цифру 1, 2 или 3")
    else:
        if 0 < select_file_format < 4:
            break
        else:
            print("Некорректный ввод! Пожалуйста, введите цифру 1, 2 или 3")

file_formats = ["JSON", "CSV", "XLSX"]

print(f"\nДля обработки выбран {file_formats[select_file_format - 1]}-файл.\n")

# чтение файла выбранного пользователем формата
if select_file_format == 1:
    transactions_info = get_transactions_info(os.path.join(ROOT_PATH, "data", "operations.json"))
elif select_file_format == 2:
    transactions_info = read_csv_file(os.path.join(ROOT_PATH, "data", "transactions.csv"))
else:
    transactions_info = read_excel_file(os.path.join(ROOT_PATH, "data", "transactions_excel.xlsx"))

# выбор статуса транзакций для фильтрации
while True:
    print(
        "Введите статус, по которому необходимо выполнить фильтрацию."
        "\nДоступные для фильтрации статусы: EXECUTED, CANCELED, PENDING")

    select_transaction_status = input().upper().strip()

    if select_transaction_status not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f'Статус операции "{select_transaction_status}" недоступен.')
    else:
        print(f'Операции отфильтрованы по статусу "{select_transaction_status}"')
        break

# фильтрация транзакций по выбранному пользователем статусу
filtered_transactions = filter_by_state(transactions_info, state=select_transaction_status)

# действия программы при наличии транзакций после фильтрации
if len(filtered_transactions):

    while True:
        sort_date = input("Отсортировать операции по дате? да/нет ").lower().strip()

        if sort_date not in ["да", "нет"]:
            print("Некорректный ввод! Пожалуйста, введите да или нет")
        else:
            break
    # выбор направления сортировки
    if sort_date == "да":
        while True:
            increasing_decreasing = input(
                "Отсортировать по возрастанию (в) или по убыванию (у)?\n Введите в или у ").lower().strip()

            if increasing_decreasing not in ["в", "у"]:
                print("Некорректрый ввод! Пожалуйста, введите в или у")
            else:
                break

        inc_dec = {"в": False, "у": True}
        sorted_transaction_by_date = sort_by_date(filtered_transactions, is_decreasing=inc_dec[increasing_decreasing])
