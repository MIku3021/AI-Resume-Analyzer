import pymysql

# Connect to MySQL database
conn = pymysql.connect(host='localhost', user='root', password='Mommyissues_123', db='cv')
cursor = conn.cursor()

# Delete all records from user_data and user_feedback tables
cursor.execute("DELETE FROM user_data")
cursor.execute("DELETE FROM user_feedback")

# Commit changes and close connection
conn.commit()
conn.close()

print("All user data and feedback have been deleted.")
