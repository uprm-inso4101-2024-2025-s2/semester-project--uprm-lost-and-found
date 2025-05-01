print("Script started")

import csv
import mysql.connector
import os

def populate_users_from_csv(csv_file_path, db_config):
    """
    Reads user data from a CSV file and inserts records into the Users table.
    """
    if not os.path.isfile(csv_file_path):
        print(f"CSV file not found: {csv_file_path}")
        return
    else:
        print(f"Found CSV file: {csv_file_path}")

    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        print("Connected to the database.")

        insert_query = """
        INSERT INTO Users (U_Username, U_Fullname, U_Email, U_Password, U_Occupation, U_ProfilePhoto)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            row_count = 0
            
            for row in csv_reader:
                print(f"Processing row: {row}")  

                cursor.execute("SELECT COUNT(*) FROM Users WHERE U_Email = %s", (row['U_Email'].strip(),))
                if cursor.fetchone()[0] > 0:
                    print(f"Skipping duplicate email: {row['U_Email']}")
                    continue

                profile_photo = None
                if 'U_ProfilePhoto' in row and row['U_ProfilePhoto'].strip():
                    photo_path = row['U_ProfilePhoto'].strip()
                    if os.path.isfile(photo_path):
                        try:
                            with open(photo_path, 'rb') as photo_file:
                                profile_photo = photo_file.read()
                        except Exception as e:
                            print(f"Warning: Could not read profile photo from '{photo_path}'. Error: {e}")
                    else:
                        print(f"Warning: Profile photo file '{photo_path}' does not exist.")


                        

                try:
                    cursor.execute(insert_query, (
                        row['U_Username'].strip(),
                        row['U_Fullname'].strip(),
                        row['U_Email'].strip(),
                        row['U_Password'].strip(),
                        row['U_Occupation'].strip(),
                        profile_photo
                    ))
                    row_count += 1
                except mysql.connector.IntegrityError as e:
                    print(f"Database rejected row due to constraint violation: {e}")
                except Exception as e:
                    print(f"Unexpected error inserting row: {e}")
            
            connection.commit()
            print(f"Successfully inserted {row_count} user(s) into the database.")

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection and connection.is_connected():
            connection.close()
        print("Database connection closed.")

if __name__ == '__main__':

    db_config = {
        'host': '127.0.0.1',               
        'user': 'root',                    
        'password': 'lost_and_found_data', 
        'database': 'LostAndFondDatabase'  
    }
    
    csv_file_path = 'C:/Users/wvele/Downloads/lostnfound/lostnfound/lostnfound/semester-project--uprm-lost-and-found/scripts/data/dummy_users.csv'
    
    populate_users_from_csv(csv_file_path, db_config)