# Assignment 15.1 SQLite
## Directions
Write a program that will read the mailbox data (mbox-long.txt) and count the number of email messages from each organizaion, per organization (i.e. domain name of the email address, like `iupui.edu`) using a database with the following schema to maintain the counts.

```
CREATE TABLE Counts (org TEXT, count INTEGER)
```

If you run the program multiple times in testing or with different files, make sure to empty out the data before each run.

You can use the included `emaildb.py` code as a starting point for your application.

The data file for this application, `mbox-long.txt` is the same as in previous assignments

The program can be speeded up greatly by moving the `conn.commit()` operation outside of the loop. In any database program, there is a balance between the number of operations you execute between commits and the importance of not losing the results of operations that have not yet been committed.

The test will be specifically looking at your `emaildb.sqlite` DB, not your string output.

## Starting Code:
```python
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
```

## Expected output after printing DB:
```
Enter file name: 
iupui.edu 536
umich.edu 491
...
ufp.pt 28
gmail.com 25
et.gatech.edu 17
```

## Testing
Once you're finished, run `pytest` to check your code!
