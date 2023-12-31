
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="#yk07db"
)

# Set the isolation level to autocommit
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Create a cursor object
cursor = conn.cursor()

# Execute a query
cursor.execute("DROP DATABASE elderco)
cursor.execute("CREATE DATABASE elderco")


#confirmation
print("all done")



# # Fetch the results
# results = cursor.fetchall()

# # Close the cursor and connection
# cursor.close()
# conn.close()