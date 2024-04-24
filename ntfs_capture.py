# ntfs_capture.py
import os
import subprocess
import argparse
from ntfs_data import insert_pcap_file, get_last_case_name

def execute_tcpdump(command, connection):
    parser = argparse.ArgumentParser(description="Packet capture utility using tcpdump")
    parser.add_argument("-c", "--count", type=int, help="Number of packets to capture", required=True)
    parser.add_argument("-i", "--interface", help="Interface to capture packets from")
    parser.add_argument("target", nargs="+", help="Target specification (e.g., src host 192.168.1.1)")
    args = parser.parse_args(command.split()[1:])
    
    case_name = get_last_case_name(connection)
    capture_packets(args.count, case_name, args.interface, " ".join(args.target), connection)

def capture_packets(packet_count, case_name, interface=None, target=None, connection=None):
    output_folder = "outputs"
    output_filename = f"{case_name}_output.pcap"
    
    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(output_folder, output_filename)

    command = ["tcpdump", "-c", str(packet_count), "-w", output_file]
    
    if interface:
        command.extend(["-i", interface])
    
    if target:
        command.extend([target])

    try:
        subprocess.run(command, check=True)
        print(f"Packets captured successfully and saved to {output_file}.")
        
        # Insert the pcap file path into the database
        insert_pcap_file(connection, output_file)
    except subprocess.CalledProcessError as e:
        print("Error capturing packets:", e)
