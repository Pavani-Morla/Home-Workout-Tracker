import sqlite3

# Connect to the database
conn = sqlite3.connect('workout.db')
cursor = conn.cursor()

# Fetch all users
cursor.execute("SELECT * FROM User")
users = cursor.fetchall()

# Display results
for user in users:
    print(user)

# Close connection
conn.close()
