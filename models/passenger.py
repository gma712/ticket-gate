from models.ticket import Ticket
from models.gate import TicketGate

class Passenger:
    def __init__(self, ticket: Ticket):
        self.__ticket = ticket

    def pass_gate(self, gate: TicketGate):
        if gate.is_passable(self.__ticket):
            print("改札を通ったよ！")
            return
        print("改札を通れないよ...")
        
