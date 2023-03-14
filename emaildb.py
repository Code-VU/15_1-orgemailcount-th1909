import sqlite3

def assignment_15_1():
    conn = sqlite3.connect('emaildb.sqlite')
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS Counts')
    cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

    filename = input('Enter file name: ')
    
    # Leave this here for testing
    if (len(filename) < 1): filename = 'mbox-long.txt'

    filehandler = open(filename)

    for line in filehandler:
        # Here you'll need you logic for cleaning the line for the org
        # And saving what you need to the DB
        
        conn.commit()

    cur.close()

if __name__ == "__main__":
    assignment_15_1()
