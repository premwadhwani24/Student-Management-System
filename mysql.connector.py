import mysql.connector
from mysql.connector import Error

# Function to fix common SQL errors
def fix_sql_error(sql_query):
    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host='localhost',
            database='students',
            user='root',
            password='prem',
            port=33066
        )
        
        cursor = connection.cursor()
        cursor.execute(sql_query)  # Execute the query
        
        # Commit changes if no error
        connection.commit()
        print("Query executed successfully!")
        
    except Error as err:
        # Handle SQL errors
        print(f"Error: {err}")
        if "syntax error" in str(err):
            print("Possible Syntax Error: Check your SQL syntax!")
            # Example of automatic fix (e.g., adding missing commas, fixing quotes)
            fixed_query = sql_query.replace(',,', ',')  # simplistic fix for duplicate commas
            print("Fixed Query: ", fixed_query)
            # Retry with the fixed query
            cursor.execute(fixed_query)
            connection.commit()
        elif "column doesn't exist" in str(err):
            print("Column missing! Check your column names in the table.")
        else:
            print("Unknown SQL error.")
    
    finally:
        # Close the connection
        if connection.is_connected():
            cursor.close()
            connection.close()

# Example SQL query with error
sql = "INSERT INTO student (rollno, sname, sem, gender, branch, email) VALUES ('1ve17cs012', 'John Doe', 3, 'Male', 'CS', 'john.doe@gmail.com')"
fix_sql_error(sql)
