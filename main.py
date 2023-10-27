
import math

class Ticket():
    def  __init__(self, id_number, start_time):
        self.id_number = id_number
        self.start_time = start_time
        self.paid = False

    def pay_for_ticket(self,end_time):
        self.time_elapsed = end_time - self.start_time

        amount = math.ceil(self.time_elapsed/15) * .50
        
        user_input = input(f'Would you like to pay {amount} \'yes\' or  \'no\' ')

        if user_input == "no":
            print("You quit the program. But you will pay eventually.")
            return
        elif user_input == "yes":
            self.paid = True 
            print("Thank you have a nice day.")
        
    def __repr__(self):
        return f"Ticket #{self.id_number} from {self.start_time} o' clock"
    
    def check_if_paid(self):
        return self.paid
    

class Parking_Garage():

    # No one in the garage, spaces are full at intialize
    def __init__(self, _max_space= 50):
        self.ticket_count = _max_space
        self.max_space = _max_space
        self.spaces_left = self.max_space
        self.current_tickets = {}
        self.tickets = []
    

    def take_ticket(self, start_time):
        print("Take ticket")
        if self.max_space > 0:
            self.spaces_left -= 1
            self.ticket_count -= 1
            print(f"Your ticket ID number is {self.ticket_count}")

            ticket = Ticket(self.ticket_count, start_time)
            self.current_tickets[str(self.ticket_count)] = ticket
            self.tickets.append(ticket)
        else:
            print("The garage is full.")

    def pay_for_parking(self):
        print("Pay for parking")
        time = float(input("enter the time:"))

        ticket_id = input("enter the ticket number").strip()

        self.current_tickets[ticket_id].pay_for_ticket(time)
    def leave_garage(self):
        ticket_id = input("enter the ticket number").strip()
        if self.current_tickets[ticket_id]:
            ticket = self.current_tickets[ticket_id]
            if ticket.check_if_paid():
                print("Thank you have a nice day")
                del self.current_tickets[ticket_id]
                self.ticket_count += 1
                self.spaces_left += 1
            else:
                self.pay_for_parking()
        else:
            print("invalid_ticket_number")


garage = Parking_Garage()

garage.take_ticket(5)

garage.pay_for_parking()
garage.leave_garage()
print(garage.current_tickets)