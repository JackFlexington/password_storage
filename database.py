# Libraries
import sqlite3

# Initialization
dbname = 'vault.db'
dbtable = 'rolodex'

# Database Functions
def create_table():
    conn = sqlite3.connect(dbname)  # Connect to database
    cur = conn.cursor() # Create a cursor object
    cur.execute('DROP TABLE IF EXISTS ' + str(dbtable))
    cur.execute('CREATE TABLE IF NOT EXISTS ' + str(dbtable) + ' (id INTEGER PRIMARY KEY, website TEXT, username TEXT, pass TEXT, email TEXT, company TEXT, sq1 TEXT, sq2 TEXT, sq3 TEXT)')
    conn.commit() # Commit changes
    conn.close() # Close connection

def insert_row(id, wbsite, user, pswd, email, company, sq1, sq2, sq3):
    conn = sqlite3.connect(dbname)  # Connect to database
    cur = conn.cursor() # Create a cursor object
    cur.execute('INSERT INTO ' + str(dbtable) + ' VALUES (?,?,?,?,?,?,?,?,?)',(id, wbsite, user, pswd, email, company, sq1, sq2, sq3))
    conn.commit() # Commit changes
    conn.close() # Close connection

def delete_row(id):
    conn = sqlite3.connect(dbname)  # Connect to database
    cur = conn.cursor() # Create a cursor object
    cur.execute('DELETE FROM ' + str(dbtable) + ' WHERE id=?',(id,)) # If only using one parameter, you need a comma ',' on the end
    conn.commit() # Commit changes
    conn.close() # Close connection

def update_row(id,wbsite,user,pswd,email,company,sq1,sq2,sq3):
    conn = sqlite3.connect(dbname)  # Connect to database
    cur = conn.cursor() # Create a cursor object
    cur.execute('UPDATE ' + str(dbtable) + ' SET website=?, username=?, pass=?, email=?, company=?, sq1=?, sq2=?, sq3=? WHERE id=?',(wbsite,user,pswd,email,company,sq1,sq2,sq3,id))
    conn.commit() # Commit changes
    conn.close() # Close connection

def view_query(search):
    conn = sqlite3.connect(dbname)  # Connect to database
    cur = conn.cursor() # Create a cursor object
    cur.execute('SELECT * FROM rolodex WHERE website=? OR username=? OR email=? OR company=?', (search,search,search,search))
    rows = cur.fetchall() # Grab all records
    conn.commit() # Commit changes
    conn.close() # Close connection
    return rows

def view_query_all():
    conn = sqlite3.connect(dbname)  # Connect to database
    cur = conn.cursor() # Create a cursor object
    cur.execute('SELECT * FROM rolodex')
    rows = cur.fetchall() # Grab all records
    conn.commit() # Commit changes
    conn.close() # Close connection
    return rows

# Initialize Table in tkinter GUI
create_table()
# Uncomment for sample values
# ID, Website, Username, Password, E-mail, Company, Security #1, Security #2, Security #3
insert_row(0,'My Bank','Jane Doe','supersecret1337','JaneDoe@techland.com','My Bank, LLC','Oldest, Middle, or Youngest child? Middle.','Street? 42 Wallaby Way','Location? Sydney')
insert_row(1,'Blizzard','John Fox','guiltyAddiction4112','JohnFox@gaming.com','Activision','Favorite Game? Cyberpunk 2077.','Favorite Programming Language? Yes.','Song? Holy Diver')
print("Printing starter test data...")
print("========================================")
print(view_query_all())
print("========================================")