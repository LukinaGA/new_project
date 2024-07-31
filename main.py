import os

from src.filter import search_dy_description
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import get_transactions_info, read_csv_file, read_excel_file
from src.widget import get_date, mask_account_card

ROOT_PATH = os.path.dirname(__file__)


def get_correct_answer(user_input: str, var_1: str, var_2: str) -> str:
    """Проверка корректности ввода пользователя для вопросов с двумя вариантами ответа"""
    while True:
        if user_input not in [var_1, var_2]:
            user_input = input(f"Некорректный ввод! Пожалуйста, введите {var_1} или {var_2}: ")
        else:
            break

    return user_input


# приветствие и выбор формата файла для работы с транзакциями
print(
    """Привет! Добро пожаловать в программу работы с банковскими транзакциями!

Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n"""
)

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
        "\nДоступные для фильтрации статусы: EXECUTED, CANCELED, PENDING"
    )

    select_transaction_state = input().upper().strip()

    if select_transaction_state not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f'Статус операции "{select_transaction_state}" недоступен.')
    else:
        print(f'Операции отфильтрованы по статусу "{select_transaction_state}"')
        break

# фильтрация транзакций по выбранному пользователем статусу
filtered_transactions_by_state = filter_by_state(transactions_info, state=select_transaction_state)

# действия программы при наличии транзакций после фильтрации
if filtered_transactions_by_state:

    sort_date = input("Отсортировать операции по дате? да/нет ").lower().strip()
    sort_date = get_correct_answer(sort_date, "да", "нет")

    # выбор направления сортировки
    if sort_date == "да":
        increasing_decreasing = input("Отсортировать по возрастанию (в) или по убыванию (у)? в/у ").lower().strip()
        increasing_decreasing = get_correct_answer(increasing_decreasing, "в", "у")

        inc_dec = {"в": False, "у": True}
        sorted_transaction_by_date = sort_by_date(
            filtered_transactions_by_state, is_decreasing=inc_dec[increasing_decreasing]
        )
    else:
        sorted_transaction_by_date = filtered_transactions_by_state

    # выбор рублёвых транзакций
    rubles_transactions = input("Выводить только рублевые тразакции? да/нет ").lower().strip()
    rubles_transactions = get_correct_answer(rubles_transactions, "да", "нет")

    if rubles_transactions == "да":
        filtered_transactions_by_rubles = filter_by_currency(sorted_transaction_by_date, "RUB")
    else:
        filtered_transactions_by_rubles = sorted_transaction_by_date

    # выбор слова для фильтрации
    if filtered_transactions_by_rubles:
        filter_by_word = (
            input("Отфильтровать список транзакций по определенному слову в описании? да/нет ").lower().strip()
        )
        filter_by_word = get_correct_answer(filter_by_word, "да", "нет")

        if filter_by_word == "да":
            search_word = input("Введите слово для фильтрации: ").lower().strip()
            filtered_transactions_by_word = search_dy_description(filtered_transactions_by_rubles, search_word)
        else:
            filtered_transactions_by_word = filtered_transactions_by_rubles

        # вывод результатов
        if filtered_transactions_by_word:
            print("\nРаспечатываю итоговый список транзакций...\n")
            print(f"Всего операций в выборке: {len(filtered_transactions_by_word)}\n")

            for transaction in filtered_transactions_by_word:
                date = get_date(transaction["date"])
                description = transaction.get("description")
                from_ = mask_account_card(transaction.get("from"))
                to_ = mask_account_card(transaction.get("to"))
                try:
                    amount = transaction["operationAmount"]["amount"]
                    currency = transaction["operationAmount"]["currency"]["name"]
                except KeyError:
                    amount = transaction.get("amount")
                    currency = transaction.get("currency_name")
                print(f"{date} {description}\n {from_} -> {to_}\n Сумма: {amount} {currency}\n")

        else:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
else:
    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
