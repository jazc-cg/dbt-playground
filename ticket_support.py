from distutils.sysconfig import customize_compiler
import string
import random
from typing import List 
from abc import ABC, abstractmethod


def generate_id(length=8):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:
    id: str
    customer: str
    issue: str
    
    def __init__(self, customer, issue) -> None:
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        pass


class FIFOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        return list.copy()


class FILOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        list_copy.reverse()
        return list_copy


class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        random.shuffle(list_copy)
        return list_copy


class BlackHoleOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        return []


class CustomerSupport:
    tickets: List[SupportTicket] = []
    
    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))
    
    def process_tickets(self, processing_strategy: TicketOrderingStrategy):
        ticket_list = processing_strategy.create_ordering(self.tickets)
        
        if len(ticket_list) == 0:
            print("There is no tickets to process.")
            return
        
        for ticket in ticket_list:
            self.process_ticket(ticket)
    
    def process_ticket(self, ticket: SupportTicket):
        print("=================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("=================================")


app = CustomerSupport()

app.create_ticket("John Smith", "My computer makes strange sounds!")
app.create_ticket("Linus Sebastian", "I can't upload any videos.")
app.create_ticket("Jae Choi", "VSCode doesn't automatically slove my bugs.")

app.process_tickets(RandomOrderingStrategy())

print("BlackHole ordering: ")
app.process_tickets(BlackHoleOrderingStrategy())
