# Task 1: Customer Service Ticket Tracker

service_tickets = {
    1: {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    2: {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}


def next_id():  # created a function that will return an id I can use to make a new service ticket
    last_id = 0
    for id in service_tickets.keys():
        if id > last_id:
            last_id = id
    return last_id + 1

def new_ticket():
    new_id = next_id()
    while True:
        customer = input("Please enter the customer name: \n")
        issue = input("Please state the issue: \n")
        print(f"Customer: {customer}, Issue: {issue}")
        correct = input("Does this information look correct? y/n ")
        if correct == 'y': # create ticket
            service_tickets[new_id] = {'Customer': customer, 'Issue': issue, 'Status': 'open'}
            break
        else: #go back to the top of the while loop (skip to the next iteration)
            
            continue

#new_ticket()


def update_ticket():
    while True:
        try: 
            update = int(input("which ticket id would you like to update? "))
            if update in service_tickets.keys():
                if service_tickets[update]['Status'] == 'open':
                    service_tickets[update]['Status'] = 'closed'
                    print(service_tickets[update])
                    break
                elif service_tickets[update]['Status'] == 'closed':
                    service_tickets[update]['Status'] = 'open'
                    print(service_tickets[update])
                    break
            else:
                print("Enter an existing ticket ID")
        except:
            print("enter numerical values only")
            continue

#update_ticket()


def display_all_tickets():
    print(service_tickets)

#display_all_tickets()


def main():
    while True:
        ans = input('''
SERVICE TICKET MANAGER
Enter the corresponding number for the action you'd like to take:
    1- Open a new service ticket.
    2- Update the status of an existing ticket  to "closed".
    3- Display all tickets.
    4 - Quit
''')
        if ans == '1':
            new_ticket() # function to add a new ticket
        elif ans == '2':
            update_ticket() # funtion to update an existing ticket
        elif ans == '3':
            print(service_tickets) # function to display all tickets
        elif ans == '4':
            print("Thanks for using service tickets manager. Have a good one!")
            break
        else:
            print("Please enter the right number")
        
main()