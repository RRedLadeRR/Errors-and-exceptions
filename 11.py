"""
Помилки (номери рядків через пробіл): !!!
"""

class NoMoneyToWithdrawError(Exception):
    def __init__(self, message):
        super().__init__(message)


class PaymentError(Exception):
    def __init__(self, message):
        super().__init__(message)


def print_accounts(accounts):
    """Друк акаунтів."""
    print("Список клієнтів ({}): ".format(len(accounts)))
    for i, (name, value) in enumerate(accounts.items(), start=1):
        print("{}. {} {}".format(i, name, value))


def transfer_money(accounts, account_from, account_to, value):
    """Виконати переказ 'value' грошей з рахунку 'account_from' на 'account_to'.

    При переказі коштів необхідно враховувати:
        - чи вистачає грошей на рахунку, з якого здійснюється переказ;
        - переказ складається зі зменшення балансу першого рахунку та збільшення
          балансу другого; якщо хоча б на одному етапі відбувається помилка,
          облікові записи повинні бути приведені в початковий стан
          (механізм транзакції)
          см. https://uk.wikipedia.org/wiki/Транзакція_(бази_даних)

    Винятки (raise):
        - NoMoneyToWithdrawError: на рахунку 'account_from'
                                  не вистачає грошей для переказу;
        - PaymentError: помилка під час переказу.
    """
    # Видаліть коментар та допишіть код


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

    print("Переклад від {account_from} для {account_to}...".
          format(**payment_info))

    payment_info["value"] = int(input("Сума = "))

    transfer_money(accounts, **payment_info)

    print("OK!")

    print_accounts(accounts)
