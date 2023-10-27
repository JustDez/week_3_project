import math
import time




class Ticket():
    def  __init__(self, id_number):
        self.id_number = id_number
        self.start_time = time.time()/60
        self.local_time = time.strftime("%H:%M:%S",time.localtime())
        self.paid = False

    def pay_for_ticket(self,end_time):
        self.time_elapsed = end_time - self.start_time

        # Charges 5 cents a minute irl

        minutes = math.ceil(float(self.time_elapsed)/60.0)
        amount = minutes * .05
        
        print(f"You've been here for {minutes} minutes at $.05 / minute")
        user_input = input(f'Would you like to pay {amount} \'yes\' or  \'no\'\n\n')

        if user_input == "no":
            print("You quit the program. But you will pay eventually.")
            return
        elif user_input == "yes":
            self.paid = True
            print("Your ticket has been paid and you have 15 minutes to leave.")


        # Shows when the ticker was bought in local time
    def __repr__(self):
        return f"Ticket #{self.id_number} from {self.local_time}."
    
    def check_if_paid(self):
        return self.paid
    

class Parking_Garage():

    # No one in the garage, spaces are full at intialize
    def __init__(self, _max_space= 50):
        self.tickets_available = _max_space
        self.max_space = _max_space
        self.spaces_left = self.max_space
        self.current_tickets = {}
        self.tickets = []
    
    

    def take_ticket(self):
        print("Take ticket")
        if self.max_space > 0:
            self.spaces_left -= 1
            self.tickets_available -= 1
            print(f"Your ticket ID number is {self.tickets_available}")

            ticket = Ticket(self.tickets_available)
            self.current_tickets[str(self.tickets_available)] = ticket
            self.tickets.append(ticket)
        else:
            print("The garage is full.")

    def pay_for_parking(self):
        print("Pay for parking")
        _time = float(time.time())/60

        ticket_id = input("enter the ticket number:   ").strip()

        self.current_tickets[ticket_id].pay_for_ticket(_time)
    def leave_garage(self):
        print("Enter ticket number to leave:")
        ticket_id = input("enter the ticket number:    ").strip()
        if self.current_tickets[ticket_id]:
            ticket = self.current_tickets[ticket_id]
            if ticket.check_if_paid():
                print("Thank you have a nice day")
                del self.current_tickets[ticket_id]
                self.tickets_available += 1
                self.spaces_left += 1
            else:
                self.pay_for_parking()
                if ticket.check_if_paid():
                    print("Thank you have a nice day")
                    del self.current_tickets[ticket_id]
                    self.tickets_available += 1
                    self.spaces_left += 1
        else:
            print("invalid_ticket_number")


garage = Parking_Garage()

garage.take_ticket()

garage.pay_for_parking()
garage.leave_garage()