from functools import wraps


def log(filename):
    """Логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception as error:
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} error: {error}. Inputs {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {error}. Inputs {args}, {kwargs}")
            else:
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} ok. Result: {result}")
                else:
                    print(f"{func.__name__} ok. Result: {result}")

        return wrapper

    return decorator
