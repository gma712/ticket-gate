from datetime import date
from models import Passenger, Ticket, TicketGate

def main():
    gate = TicketGate(
        min_fare=180
    )
    ticket = Ticket(
        fare=200,
        expiry_date=date(year=2022, month=9, day=20)
    )
    passenger = Passenger(
        ticket=ticket
    )
    passenger.pass_gate(gate)


if __name__ == '__main__':
    main()
