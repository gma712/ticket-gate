from datetime import date

class Ticket:
    def __init__(self, fare: int, expiry_date: date):
        self.__fare = fare
        self.__expiry_date = expiry_date

    @property
    def fare(self):
        return self.__fare

    @property
    def is_expired(self) -> bool:
        return date.today() > self.__expiry_date
