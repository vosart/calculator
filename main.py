import datetime as dt
from dateutil.parser import parse
from datetime import timedelta

date_format = '%d.%m.%Y'
now = dt.datetime.now().strftime(date_format)


class Record:
    def __init__(self, amount, comment, date=now):
        self.amount = amount
        self.date = date
        self.comment = comment


class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []
    def add_record(self, all_recs):
        self.records.append(all_recs)


    def get_today_stats(self):
        stat_today = 0
        for recs in self.records:
            if recs.date == now:
                stat_today += recs.amount
        print(f'Amount today: {stat_today}')
        return stat_today

#расчет трат за неделю

    def get_week_stats(self):
        stat_week = 0
        for recs in self.records:
            a_day = parse(recs.date, dayfirst=True)
            if parse(now) >= a_day >= (parse(now) - timedelta(6)):
                stat_week += recs.amount
        print(f'Amount for week: {stat_week}')
        return stat_week




class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        if self.limit > 0:
            answer = f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit - self.get_today_stats()} кКал'
        elif self.limit < 0:
            answer = 'Хватит есть!'
        return answer

class CashCalculator(Calculator):
    USD_RATE = 74.39
    EURO_RATE = 81.7

    def get_today_cash_remained(self, currency="rub"):
        # usd, euro, rub
        self.currency = currency
        if self.currency == 'usd':
            self.limit /= self.USD_RATE
        elif self.currency == 'euro':
            self.limit /= self.EURO_RATE
        if self.limit == 0:
            print(f'Денег нет, держись!')
        elif self.limit < 0:
            print(f'Денег нет, держись! Твой долг: {round(self.limit, 2)} {currency}')
        else:
            print(f'На сегодня осталось: {round(self.limit, 2)} {currency}')



if __name__ == '__main__':
    cash_calculator = CashCalculator(1000)
    cash_calculator.add_record(Record(amount=140, comment="coffee"))
    cash_calculator.add_record(Record(amount=300, comment="coffee"))
    cash_calculator.add_record(Record(amount=300, comment="coffee"))
    cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="02.02.2021"))
    cash_calculator.add_record(Record(amount=15, comment="бар в Танин др", date="01.02.2021"))
    cash_calculator.add_record(Record(amount=1007, comment="бар в Санин др", date="03.02.2021"))
    cash_calculator.add_record(Record(amount=100, comment="бар в Данин др", date="27.01.2021"))
    cash_calculator.add_record(Record(amount=500, comment="выпечка", date="19.12.2020"))
    cash_calculator.get_today_cash_remained("usd")
    cash_calculator.get_today_stats()
    cash_calculator.get_week_stats()

    calories_calculator = CaloriesCalculator(3000)
    calories_calculator.add_record(Record(amount=40, comment="coffee"))
    calories_calculator.add_record(Record(amount=2000, comment="coffee"))
    calories_calculator.add_record(Record(amount=100, comment="coffee"))
    calories_calculator.add_record(Record(amount=100, comment="Тортег в кафе", date="27.01.2021"))
    calories_calculator.add_record(Record(amount=100, comment="Тортег в кафе", date="26.01.2021"))
    calories_calculator.get_today_stats()
    calories_calculator.get_week_stats()
    print(calories_calculator.get_calories_remained())
