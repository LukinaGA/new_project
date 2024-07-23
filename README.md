# Виджет банковских операций клиента

## Описание

Виджет для отображения банковских опрераций клиента и работы с ними(сортировки, фильтрации)

## Содержание

Виджет содержит 7 рабочих модулей:
1. **masks**, который принимает номер карты или счёта и возвращает их маску 
```
7000792289606361 => 7000 79** **** 6361    # номер карты
73654108430135874305 => **4305             # номер счёта
```
В модуле присутствует логирование, результаты которого записываются в файл masks.log в папке logs
2. **widget**, возвращающий маску счёта или карты, исходя из полученных данных
```
Maestro 1596837868705199 => Maestro 1596 83** **** 5199
Счет 73654108430135874305 => Счет **4305
```
и отображающий дату в формате ДД.ММ.ГГГГ
```
2024-03-11T02:26:18.671407 => 11.03.2024
```
3. **processing** для фильтрации транзакций по статусу и сортировки по дате
4. **generators** фильтрует транзакции по заданной валюте, возвращает описание каждой операции, генерирует номер карты в заданном диапазоне
```
>>> 0000 0000 0000 0002    # для генерации номера карты
    0000 0000 0000 0003    # задаём диапазон от 2 до 4  
    0000 0000 0000 0004     
```
5. **decorators**, в котором хранится декоратор для логирования начала и конца выполнения функции, а также ее результатов или возникших ошибок. Если указано имя файла, результаты выполнения должны быть записаны в это файл. Если имя не указано - выведены в консоль
```
my_function ok. Result = result                              # ожидаемый вывод при успешном выполнении
my_function error: текст ошибки. Inputs: (arg1, arg2), {}    # ожидаемый вывод при ошибке
```
6. **utils**, открывающий json-файл для работы с транзакциями.
В модуле присутствует логирование, результаты которого записываются в файл utils.log в папке logs
7. **external_api** получает транзакцию и возвращает сумму транзакции в рублях (при необходимости конвертирует другие валюты в рубли). Для конвертации использует [APILayer](https://apilayer.com/marketplace/exchangerates_data-api)
## Тестировние
В директории test прописаны тесты для каждого модуля из диктории src.
Также здесь есть модуль conftest.py с фикстурами для тестов. Code coverage = 95%