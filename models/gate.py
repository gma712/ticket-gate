from models.ticket import Ticket

class TicketGate:

    def __init__(self, min_fare):
        self.__min_fare = min_fare

    def is_passable(self, ticket: Ticket) -> bool:
        if ticket.is_expired:
            return False
        return True
