#description - requests tickets from account using Zendesk API and lists them in pages or detailed view if credentials are authorized.

import requests
import os
 
#function that makes a system call to clear screen #
def clear():
    if os.name in ('nt','dos'):
        os.system('cls')
    else:
        os.system('clear')

# Set the request parameters
user = 'natnaelteshome@my.unt.edu'
pwd = 'T$m2021'

#menu
def menu():
    print("\n\t\tPlease select menu option:")
    print("\t\t  * Enter 1 to view all tickets")
    print("\t\t  * Enter 2 to view a ticket")
    print("\t\t  * Enter 0 to exit program")

#queries all tickets in account and prints them by page
def SearchAllTickets():
    url = 'https://zccmy.zendesk.com/api/v2/tickets.json'
    print ("\nid \tstatus\t created on\t\tsubject\n")
    count = 0
    getnexturl = True
    while url:
        response = requests.get(url, auth=(user, pwd))
        #catches http request errors
        if response.status_code != 200:
            print('Status:', response.status_code, 'Problem with the request. Exiting...')
            exit()
        data = response.json()
        ticket_list = data['tickets']
        for ticket in ticket_list:
            count += 1
            print(str(ticket['id']).ljust(5) + " \t" + ticket['status'].center(2) + " \t"  + ticket['created_at']) + "\t" + ticket['subject'] #print basic fields for listing
            if(count == 25): #paging mechanism
                print("\nenter 1 to go to the next page")
                print("enter 2 to view a ticket")
                print("enter 0 to go back to main menu\n")
                x = raw_input() #input for secondary menu
                try:
                    int(x)
                except:
                    print("Expected number 0 - 2")
                if(x == '1'):
                    print("\nenter 1 to go to the next page")
                    print("enter 2 to view a ticket")
                    print("enter 0 to go back to main menu\n")
                    clear() #clear screen and present another 25 results
                    count = 0 #reset counter
                elif(x == '2'): #giving user option to look at a ticket in more detail
                    z = raw_input("enter ticket id: ")
                    try:
                        int(z)
                    except:
                        print("invalid input. try again")
                        getnexturl = False
                        break
                    LookUpTicket(z)
                    getnexturl = False
                    break
                elif(x == '0'):
                    getnexturl = False
                    break
                else:
                    print("invalid input. try again")
                    getnexturl = False
                    break
        if(getnexturl == True):    
            url = data['next_page']  #get next page
        else:
            url = None   
      

#function for looking up tickets by thier ID
def LookUpTicket(ticketnum):
    url = "https://zccmy.zendesk.com/api/v2/tickets/" + str(ticketnum) + ".json"
    response = requests.get(url, auth=(user, pwd))
    if response.status_code != 200:
        print('Status:', response.status_code, "Problem with the request. Tickest probably doesn't exist. try again")
        #exit()
    else:    
        data = response.json()

        print("\nTicket Type -> " + str(data['ticket']['type']))
        print("Status -> " + data['ticket']['status'])
        print("Ticket subject -> " + data['ticket']['subject'])
        print("Ticket ID -> " + str(data['ticket']['id']))
        print("Priority -> " + str(data['ticket']['priority']))
        print("Created at ->" + str(data['ticket']['created_at']))
        print("Assignee ID -> " + str(data['ticket']['assignee_id']))
        print("submitter ID -> " + str(data['ticket']['submitter_id']))
        print("Group ID -> " + str(data['ticket']['group_id']))
        print("Requester ID -> " + str(data['ticket']['requester_id']))
        print("Description -> " + data['ticket']['description'])
        return data

def main():
    print("\n\t\tZendesk TicketViewer\n".center(20))
    while True:
        menu()
        y = raw_input()
        try:
            vars = int(y)
        except:
            print("\n")
        if(y == '1'):
            SearchAllTickets()
        elif (y == '2'):
            ticketid = raw_input('\nEnter ticket id: ')
            try:
                int(ticketid)
                LookUpTicket(ticketid)
            except:
                print("ticket id does not exist. Exiting...")
                break
                
        elif (y == "0"):
            print("\nThank you for you using my Ticketviewer. GoodBye!\n")
            break
        else:
            print("invalid input! please follow the directions in the menu!")
            

if __name__ == "__main__":
    main()
