from src.decorators import log


def test_log_empty_filename_ok(capsys):
    @log(filename="")
    def adds(x, y):
        return x + y

    adds(1, 2)

    captured = capsys.readouterr()
    assert captured.out == "adds ok. Result: 3\n"


def test_log_filename_ok(capsys):
    @log(filename="mylog.txt")
    def adds(x, y):
        return x + y

    adds(1, 2)

    captured = capsys.readouterr()
    assert captured.out == ""

    with open("mylog.txt", "r") as file:
        print(file.read())

    captured = capsys.readouterr()
    assert captured.out == "adds ok. Result: 3\n"


def test_log_empty_filename_error(capsys):
    @log(filename="")
    def divide(x, y):
        return x / y

    divide(1, 0)

    captured = capsys.readouterr()
    assert captured.out == "divide error: division by zero. Inputs (1, 0), {}\n"


def test_log_filename_error(capsys):
    @log(filename="mylog.txt")
    def divide(x, y):
        return x / y

    divide(1, 0)

    captured = capsys.readouterr()
    assert captured.out == ""

    with open("mylog.txt", "r") as file:
        print(file.read())

    captured = capsys.readouterr()
    assert captured.out == "divide error: division by zero. Inputs (1, 0), {}\n"
