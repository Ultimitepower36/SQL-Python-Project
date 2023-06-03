import mysql.connector
from mysql.connector import Error
import mysql



create_person_table = """
CREATE TABLE IF NOT EXISTS person (
  person_id INT PRIMARY KEY,
  first_name VARCHAR(40) NOT NULL,
  last_name VARCHAR(40) NOT NULL,
  interest_1 VARCHAR(20) NOT NULL,
  interest_2 VARCHAR(20)
  );
 """

pop_person = """
INSERT INTO person VALUES
(1,  'James', 'Smith', 'Art', NULL),
(2, 'Stefanie',  'Martin',  'Rock', NULL), 
(3, 'Steve', 'Wang', 'Legos', 'Nintendo');

"""


create_hobby_table = """
CREATE TABLE IF NOT EXISTS hobby (
  hobby_id INT PRIMARY KEY,
  hobby_1 VARCHAR(20) NOT NULL,
  hobby_2 VARCHAR(20)
);
 """

pop_hobby = """
INSERT INTO hobby VALUES
(1,  'Boxing', NULL),
(2, 'Knitting',  'Jogging'), 
(3, 'Soccer', NULL);

"""

def main():
    pw = input ("What is the password to the database?\n")
    db = input ("What is the name of the database?\n")
    #first time set up
    connection = create_server_connection("localhost", "root", pw, db)

    setup_main(connection)
    more = "yes"
    while (more.lower() != "no"):
        input_1 = input("What would you like to do? (INSERT, MODIFY, DELETE, or RETRIEVE)\n")
        if(input_1.upper() == "INSERT"):
            input_2 = input("Which table do you want to insert into?\n")
            input_3 = input("What should be added? (formated like: 4, x, y,...)\n")

            insert = f"""
            INSERT INTO {input_2} VALUES
            ({input_3});
            """
            execute_query(connection, insert)
            more = input("Continue? (yes or no)\n")

        elif(input_1.upper() == "MODIFY"):
            input_2 = input("Which table do you want to modify?\n")
            input_3 = input("Which row do you want to modify?\n")
            input_4 = input("Which column do you want to modify?\n")
            input_5 = input("What do you want put there?\n")

            update = f"""
            UPDATE {input_2} 
            SET {input_4} = {input_5}] 
            WHERE client_id = {input_3};
            """
            execute_query(connection, update)
            more = input("Continue? (yes or no)\n")
            
        elif(input_1.upper() == "DELETE"):
            input_2 = input("Which table do you want to delete from?\n")
            input_3 = input("Which row do you want to delete from?\n")

            delete_row = f"""
            DELETE FROM {input_2} 
            WHERE course_id = {input_3};
            """
            execute_query(connection, delete_row)
            more = input("Continue? (yes or no)\n")

        elif(input_1.upper() == "RETRIEVE"):
            input_2 = input("Which table do you want to see?\n")

            q = f""" SELECT * FROM {input_2}; """
            results = read_query(connection, q)
            for result in results:
                print(result)
            more = input("Continue? (yes or no)\n")
        else:
            print("That is not a valid entry, please try again.")
            more = input("Continue? (yes or no)\n")
    print("Thanks for using this software, have a nice day.")

def setup_main(connection):
    execute_query(connection, create_person_table)
    execute_query(connection, create_hobby_table)
    execute_query(connection, pop_person)
    execute_query(connection, pop_hobby)


def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    #error handler
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

main()