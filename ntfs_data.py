# ntfs_data.py
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
    return None

def create_registration_table(connection):
    create_registration_table_sql = """CREATE TABLE IF NOT EXISTS registration (
                                        id INTEGER PRIMARY KEY,
                                        CaseName TEXT NOT NULL,
                                        OrganizationName TEXT NOT NULL,
                                        InvestigatorsName TEXT NOT NULL,
                                        Date DATE NOT NULL
                                    );"""
    try:
        cursor = connection.cursor()
        cursor.execute(create_registration_table_sql)
    except Error as e:
        print(e)

def create_pcap_file_table(connection):
    create_pcap_file_table_sql = """CREATE TABLE IF NOT EXISTS pcap_file (
                                        id INTEGER PRIMARY KEY,
                                        RegistrationID INTEGER NOT NULL,
                                        FilePath TEXT NOT NULL,
                                        FOREIGN KEY (RegistrationID) REFERENCES registration(id)
                                    );"""
    try:
        cursor = connection.cursor()
        cursor.execute(create_pcap_file_table_sql)
    except Error as e:
        print(e)

def insert_registration(connection, case_name, organization, investigator_name, current_date):
    sql_query = """INSERT INTO registration (CaseName, OrganizationName, InvestigatorsName, Date) 
                   VALUES (?, ?, ?, ?)"""
    data = (case_name, organization, investigator_name, current_date)
    try:
        cursor = connection.cursor()
        cursor.execute(sql_query, data)
        connection.commit()
        print("Case registration successful and saved to the database!")
    except Error as e:
        print("Error inserting data:", e)

def insert_pcap_file(connection, file_path):
    sql_query = """INSERT INTO pcap_file (RegistrationID, FilePath) 
                   VALUES (?, ?)"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_query, (get_last_registration_id(connection), file_path))
        connection.commit()
    except Error as e:
        print("Error inserting PCAP file:", e)

def get_last_registration_id(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT max(id) FROM registration")
    row = cursor.fetchone()
    if row[0]:
        return row[0]
    else:
        print("No registrations found.")
        return None

def get_last_case_name(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT CaseName FROM registration ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    if row:
        return row[0]
    else:
        print("No cases found.")
        return None
