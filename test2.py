import main
import random
import time
import math
# Spin off of Parking Garage functionality
class Parking_Garage2(main.Parking_Garage):
    
    # No one in the garage, spaces are full at intialize
    def __init__(self, _max_space= 50, payrate = .05):
        self.payrate = payrate
        self.tickets_given = 0
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
            self.tickets_given += 1
            

            # Creates a unique random ticket ID
            id_number = str(self.tickets_given)+"_"+str(random.randint(1,1000))+chr(random.randint(97,122)).upper()

            print(f"Your ticket ID number is {id_number}")

            ticket = main.Ticket(id_number)
            self.current_tickets[str(id_number)] = ticket
            self.tickets.append(ticket)
        else:
            print("The garage is full.")


    def leave_garage(self):
        print("Enter ticket number to leave:")
        ticket_id = input("enter the ticket number:    ").strip()
        if ticket_id in self.current_tickets:
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

class Premium_parking(Parking_Garage2):
    def __init__(self, _max_space=50, premium_payrate=0.07, max_premium_spaces=5):
        self.premium_spaces_left = max_premium_spaces
        self.premium_tickets_available = max_premium_spaces
        self.tickets_available = _max_space
        self.max_space = _max_space
        self.spaces_left = self.max_space
        self.current_tickets = {}
        self.tickets = []
        self.premium_tickets = {}
        self.premium_payrate = premium_payrate
        self.max_premium_spaces = max_premium_spaces
        self.max_space -= self.max_premium_spaces
        self.tickets_given = 0
        self.payrate = premium_payrate



    def add_customer_info(self, ticket_id, data):
        if ticket_id in self.current_tickets:
            self.premium_tickets[ticket_id] = ticket_info

    def pay_for_parking(self):
        print("Pay for premium parking")
        _time = float(time.time())/60

        ticket_id = input("enter the ticket number:   ").strip()

        self.current_tickets[ticket_id].pay_for_ticket(_time)

    def take_premium_ticket(self):
        
        print("Take premium ticket")
        if self.premium_spaces_left > 0:
            self.premium_spaces_left -= 1
            self.premium_tickets_available -= 1
            id_number = str(self.tickets_given)+"_"+str(random.randint(1,1000))+chr(random.randint(97,122)).upper()

            print(f"Your ticket Premium ticket ID number is {id_number}")
           

            ticket = Premium_tickets(id_number, payrate=self.payrate)
            self.current_tickets[str(id_number)] = ticket
            self.tickets.append(ticket)
        else:
            print("The premium spaces are full.")


class Premium_tickets(main.Ticket):
    def __init__(self, id_number, payrate=0.07):
        self.payrate= payrate
        super().__init__(id_number)
    def pay_for_ticket(self,end_time):
        self.time_elapsed = end_time - self.start_time

        # Charges 7 cents a minute irl

        minutes = math.ceil(float(self.time_elapsed)/60.0)
        amount = minutes * self.payrate
        
        print(f"You've been here for {minutes} minutes at ${self.payrate} / minute")
        user_input = input(f'Would you like to pay {amount} \'yes\' or  \'no\'\n\n')

        if user_input == "no":
            print("You quit the program. But you will pay eventually.")
            return
        elif user_input == "yes":
            self.paid = True
            print("Your ticket has been paid and you have 15 minutes to leave.")
         


garage2 = Premium_parking()

garage2.take_premium_ticket()
garage2.leave_garage()
