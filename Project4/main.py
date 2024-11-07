# main.py

import json
import requests


# Определение пользовательских исключений
class InsufficientBalanceError(Exception):
    pass


class InvalidAccountNumberError(Exception):
    pass


class TransactionLimitExceededError(Exception):
    pass


# Функции для демонстрации работы исключений

def divide(a, b):
    # Шаг 1: Функция для деления двух чисел
    return a / b


def get_element(lst, index):
    # Шаг 1: Функция для получения элемента из списка
    return lst[index]


def safe_divide(a, b):
    # Шаг 2: Функция для безопасного деления с обработкой исключения
    try:
        result = a / b
        print(f"Результат деления: {result}")
        return result
    except Exception as e:
        print(f"Произошла ошибка при делении: {str(e)}")
        return None


def file_operation(filename):
    # Шаг 3: Функция для работы с файлом с блоком finally
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Содержимое файла: {content}")
            return content
    except Exception as e:
        print(f"Произошла ошибка при работе с файлом: {str(e)}")
        return None
    finally:
        print("Операция с файлом завершена.")


def complex_operation(a, b):
    # Шаг 4: Функция с несколькими обработчиками исключений
    try:
        result = a / b
        print(f"Результат деления: {result}")
        return result
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль!")
        return None
    except TypeError:
        print("Ошибка: Некорректный тип данных для операции.")
        return None
    except Exception as e:
        print(f"Неожиданная ошибка: {str(e)}")
        return None
    finally:
        print("Операция завершена.")


def list_operation(lst):
    # Шаг 4: Функция для работы со списком с несколькими обработчиками исключений
    try:
        result = lst[5] / 2
        print(f"Результат операции: {result}")
        return result
    except IndexError:
        print("Ошибка: Индекс списка вышел за пределы.")
        return None
    except TypeError:
        print("Ошибка: Некорректный тип данных для операции.")
        return None
    except Exception as e:
        print(f"Неожиданная ошибка: {str(e)}")
        return None
    finally:
        print("Операция со списком завершена.")


def dictionary_operation(dct):
    # Шаг 4: Функция для работы со словарем с несколькими обработчиками исключений
    try:
        result = dct['key'] / 2
        print(f"Результат операции: {result}")
        return result
    except KeyError:
        print("Ошибка: Ключ не найден в словаре.")
        return None
    except TypeError:
        print("Ошибка: Некорректный тип данных для операции.")
        return None
    except Exception as e:
        print(f"Неожиданная ошибка: {str(e)}")
        return None
    finally:
        print("Операция со словарем завершена.")


def raise_exceptions(value):
    # Шаг 5: Функция для генерации различных исключений
    try:
        if value < 0:
            raise ValueError(f"Значение {value} меньше нуля.")
        elif value == 0:
            raise ZeroDivisionError("Деление на ноль!")
        elif isinstance(value, str):
            raise TypeError("Некорректный тип данных: строка.")
        else:
            result = 100 / value
            print(f"Результат операции: {result}")
            return result
    except ValueError as ve:
        print(f"Ошибка значения: {str(ve)}")
    except ZeroDivisionError as zde:
        print(f"Ошибка деления на ноль: {str(zde)}")
    except TypeError as te:
        print(f"Ошибка типа: {str(te)}")
    except Exception as e:
        print(f"Неожиданная ошибка: {str(e)}")
    finally:
        print("Операция завершена.")


def bank_transaction(account_number, balance, amount):
    # Шаг 7: Функция для банковской транзакции с пользовательским исключением
    try:
        if account_number <= 0:
            raise InvalidAccountNumberError("Неверный номер счета.")
        if balance < amount:
            raise InsufficientBalanceError("Недостаточно средств на счете.")
        if amount > 10000:
            raise TransactionLimitExceededError("Превышен лимит транзакции.")

        new_balance = balance - amount
        print(f"Транзакция успешно выполнена. Новый баланс: {new_balance}")
        return new_balance
    except InvalidAccountNumberError as iane:
        print(f"Ошибка счета: {str(iane)}")
    except InsufficientBalanceError as ibe:
        print(f"Ошибка баланса: {str(ibe)}")
    except TransactionLimitExceededError as tle:
        print(f"Ошибка лимита транзакции: {str(tle)}")
    finally:
        print("Операция с банковским счетом завершена.")


def calculate_statistics(data):
    # Функция для расчета статистики с обработкой исключений
    try:
        mean = sum(data) / len(data)
        median = sorted(data)[len(data) // 2] if len(data) % 2 != 0 else (sorted(data)[len(data) // 2 - 1] +
                                                                          sorted(data)[len(data) // 2]) / 2
        mode = max(set(data), key=data.count)

        print(f"Среднее значение: {mean}")
        print(f"Медиана: {median}")
        print(f"Мода: {mode}")
        return mean, median, mode
    except ZeroDivisionError:
        print("Ошибка: Пустой список данных.")
        return None, None, None
    except Exception as e:
        print(f"Неожиданная ошибка при расчете статистики: {str(e)}")
        return None, None, None


def parse_json(json_string):
    # Функция для парсинга JSON с обработкой исключений
    try:
        data = json.loads(json_string)
        print(f"Парсинг JSON успешен. Полученные данные: {data}")
        return data
    except json.JSONDecodeError as jde:
        print(f"Ошибка декодирования JSON: {str(jde)}")
        return None
    except Exception as e:
        print(f"Неожиданная ошибка при парсинге JSON: {str(e)}")
        return None


def network_request(url):
    # Функция для сетевого запроса с обработкой исключений
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"Запрос к {url} успешен. Статус код: {response.status_code}")
        return response.text
    except requests.RequestException as re:
        print(f"Ошибка сетевого запроса: {str(re)}")
        return None
    except Exception as e:
        print(f"Неожиданная ошибка при выполнении сетевого запроса: {str(e)}")
        return None


# Основная функция для демонстрации работы исключений
def main():
    print("Начало демонстрации работы исключений:")

    # Демонстрация шагов 1-8
    divide(10, 2)
    get_element([1, 2, 3], 1)
    safe_divide(5, 0)
    file_operation("example.txt")
    complex_operation(10, 2)
    list_operation([1, 2, 3])
    dictionary_operation({"key": 10})
    raise_exceptions(-5)
    bank_transaction(12345, 1000, 500)
    calculate_statistics([1, 2, 3, 4, 5])
    parse_json('{"key": "value"}')
    network_request("http://example.com")

    print("\nКонец.")


if __name__ == "__main__":
    main()
