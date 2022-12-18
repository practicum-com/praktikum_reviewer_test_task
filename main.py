import datetime as dt


class Record:
    # Create getter methods for date and amount

    def __init__(self, amount, comment, date=''):
        # date parameter can contain a default value (today)
        self.amount = amount
        # I suggest to create a new method to validate the date passed as parameter
        self.date = (
            dt.datetime.now().date() if
            not
            date else dt.datetime.strptime(date, '%d.%m.%Y').date())
        self.comment = comment


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    # get_today_stats => we can create a new method inside Record class to check if a record was created Today
    # instead of doing the calculations inside this method
    def get_today_stats(self):
        today_stats = 0
        # Create getter methods for date and amount
        # Record is a class not an object so this iteration will not work
        for Record in self.records:
            if Record.date == dt.datetime.now().date():
                # this will not work, use limit variable instead to calculate 'today_stats'
                today_stats = today_stats + Record.amount
        return today_stats

    # get_week_stats => We can create a new method inside 'Record' class
    # to check if a record belongs to the last 7 days
    def get_week_stats(self):
        week_stats = 0
        today = dt.datetime.now().date()
        for record in self.records:
            # create variables, fix logic it is hard to read
            if (
                    (today - record.date).days < 7 and
                    (today - record.date).days >= 0
            ):
                week_stats += record.amount
        return week_stats


class CaloriesCalculator(Calculator):
    # Review Docstring Conventions to document methods
    def get_calories_remained(self):  # Gets the remaining calories for today
        x = self.limit - self.get_today_stats()
        # x ?? create more meaningful variable names
        if x > 0:
            # fix message:  'Today you can eat some...'
            return f'You can eat something else today,' \
                   f' but with a total calorie content of no more than {x} kcal'
        else:
            # remove redundant parentheses
            return ('Stop eating!')


class CashCalculator(Calculator):
    USD_RATE = float(60)  # US dollar exchange rate.
    EURO_RATE = float(70)  # Euro exchange rate.

    # parameter names should be lowercase
    def get_today_cash_remained(self, currency,
                                USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        # redundant variable currency_type
        currency_type = currency

        cash_remained = self.limit - self.get_today_stats()
        # Having too many if else statements makes it hard to read,
        # create a dictionary instead to calculate cash_remained based on te currency_type
        if currency == 'usd':
            # Create static variables for each currency
            cash_remained /= USD_RATE
            currency_type = 'USD'
        elif currency_type == 'eur':
            cash_remained /= EURO_RATE
            currency_type = 'Euro'
        elif currency_type == 'rub':
            cash_remained == 1.00
            currency_type = 'rub'
        if cash_remained > 0:
            return (
                f'Left for today {round(cash_remained, 2)} '
                f'{currency_type}'
            )
        elif cash_remained == 0:
            # if it is 0 should return 'there is no money...'
            return 'No money, keep it up!'
        elif cash_remained < 0:
            return 'No money, keep it up:' \
                   ' your debt is - {0:.2f} {1}'.format(-cash_remained,
                                                        currency_type)

    # Missing return statement
    def get_week_stats(self):
        super().get_week_stats()
