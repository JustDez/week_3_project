
import math

class Ticket():
    def  __init__(self, id_number, start_time):
        self.id_number = id_number
        self.start_time = start_time

    def pay_for_ticket(self,end_time):
        self.time_elapsed = end_time - self.start_time

        amount = math.ceil(self.time_elapsed/15) * .50
        
        user_input = input('Would you like to pay amount \'yes\' or  \'no\' ')

        if user_input == "no":
            print("You quit the program. But you will pay eventually.")
            return
        elif user_input == "yes":
            print("Thank you have a nice day.")
        
    def __repr__(self):
        return f"Ticket #{self.id_number} from {self.start_time} o' clock"

class Parking_Garage():

    # No one in the garage, spaces are full at intialize
    def __init__(self, _max_space= 50):
        self.ticket_count = _max_space
        self.max_space = _max_space
        self.spaces_left = self.max_space
        self.current_tickets = {}
        self.tickets = []
    

    def take_ticket(self, start_time):
        if self.max_space > 0:
            self.spaces_left -= 1
            self.ticket_count -= 1

            ticket = Ticket(self.ticket_count, start_time)
            self.current_tickets[str(self.ticket_count)] = ticket
            self.tickets.append(ticket)
        else:
            print("The garage is full.")

    def pay_for_parking(self):
        time = float(input("enter the time:"))

        ticket_id = float(input("enter the ticket number"))

        self.current_tickets[ticket_id].pay_for_ticket(time)



garage = Parking_Garage()

garage.take_ticket(5)

garage.pay_for_parking()
