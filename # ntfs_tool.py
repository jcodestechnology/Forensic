# ntfs_tool.py
import argparse
from ntfs_display import clear_screen, display_figlet_with_lolcat
from ntfs_registration import register_case
from ntfs_capture import execute_tcpdump
from ntfs_data import create_connection, create_registration_table, create_pcap_file_table

def main():
    clear_screen()
    display_figlet_with_lolcat("Network Forensic Tool", "standard")
    display_figlet_with_lolcat("Get DDOS report", "digital")

    db_file = "ntfs.db"
    connection = create_connection(db_file)
    if connection is not None:
        create_registration_table(connection)
        create_pcap_file_table(connection)

    case_registered = False

    while True:
        if not case_registered:
            print("\n1. Register Case")
            print("2. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                register_case(connection)
                case_registered = True
            elif choice == '2':
                print("Exiting...")
                if connection:
                    connection.close()
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            command = input("\nEnter command: ")
            if command.startswith("ntfs "):
                execute_tcpdump(command, connection)
            else:
                print("Invalid command. Commands must start with 'ntfs'.")

if __name__ == "__main__":
    main()
