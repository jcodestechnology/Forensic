# ntfs_registration.py
import datetime
from ntfs_data import insert_registration
from ntfs_display import clear_screen, display_figlet_with_lolcat

def register_case(connection):
    case_name = input("Enter the case name: ")
    organization = input("Enter the organization: ")
    investigator_name = input("Enter the investigator name: ")
    
    current_date = datetime.date.today()
    
    insert_registration(connection, case_name, organization, investigator_name, current_date)

    clear_screen()
    display_figlet_with_lolcat("Network Forensic Tool", "standard")
    display_figlet_with_lolcat("Get DDOS report", "digital")
    print("\nEnter command:")
