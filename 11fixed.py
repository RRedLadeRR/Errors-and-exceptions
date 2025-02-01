"""
Помилки (номери рядків через пробіл, цей рядок - №2): 41 66
"""

class NoMoneyToWithdrawError(Exception):
    def __init__(self, message):
        super().__init__(message)


class PaymentError(Exception):
    def __init__(self, message):
        super().__init__(message)


def print_accounts(accounts):
    """Друк акаунтів."""
    print("Список клієнтів ({}):".format(len(accounts)))
    for i, (name, value) in enumerate(accounts.items(), start=1):
        print("{}. {} {}".format(i, name, value))


def transfer_money(accounts, account_from, account_to, value):
    """Виконати переказ 'value' грошей з рахунку 'account_from' на 'account_to'.

    Винятки:
        - NoMoneyToWithdrawError: недостатньо коштів;
        - PaymentError: помилка під час операції.
    """
    if account_from not in accounts or account_to not in accounts:
        raise PaymentError("Помилка: одного з акаунтів не існує.")

    if accounts[account_from] < value:
        raise NoMoneyToWithdrawError("Недостатньо коштів на рахунку {}!".format(account_from))

    # Транзакційний механізм
    try:
        original_from = accounts[account_from]
        original_to = accounts[account_to]

        # Знімаємо гроші
        accounts[account_from] -= value

        # Імітуємо можливу помилку при переказі
        if accounts[account_from] < 0:  
            raise PaymentError("Помилка під час переказу грошей.")

        # Додаємо гроші
        accounts[account_to] += value

    except PaymentError as e:
        # Відкат змін у разі помилки
        accounts[account_from] = original_from
        accounts[account_to] = original_to
        print(e)


if __name__ == "__main__":
    accounts = {
        "Василь Іванов": 100,
        "Іван Васильєв": 1500,
        "Петро Бондаренко": 400
    }
    print_accounts(accounts)

    payment_info = {
        "account_from": "Василь Іванов",
        "account_to": "Іван Васильєв"
    }

    print("Переказ від {account_from} для {account_to}...".format(**payment_info))

    try:
        payment_info["value"] = int(input("Сума = "))  # Може викликати ValueError
        transfer_money(accounts, **payment_info)
        print("OK!")
    except ValueError:
        print("Помилка: введене значення не є числом.")
    except (NoMoneyToWithdrawError, PaymentError) as e:
        print(e)

    print_accounts(accounts)
