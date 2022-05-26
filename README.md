## Counting Emails per Organizations
This application will read the mailbox data (mbox-long.txt) and count the number of email messages from each organizaion, per organization (i.e. domain name of the email address, like `iupui.edu`) using a database with the following schema to maintain the counts.

```
CREATE TABLE Counts (org TEXT, count INTEGER)
```

If you run the program multiple times in testing or with different files, make sure to empty out the data before each run.

You can use the included `emaildb.py` code as a starting point for your application/

The data file for this application, `mbox-long.txt` is the same as in previous assignments

Because the sample code is using an UPDATE statement and committing the results to the database as each record is read in the loop, it might take as long as a few minutes to process all the data. The commit insists on completely writing all the data to disk every time it is called.

The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program, there is a balance between the number of operations you execute between commits and the importance of not losing the results of operations that have not yet been committed.

The test will be specifically looking at your `emaildb.sqlite` DB


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