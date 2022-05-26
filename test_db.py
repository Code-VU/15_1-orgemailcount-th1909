import sqlite3
import pytest

def test_long_mbox(capfd):
    conn = sqlite3.connect('emaildb.sqlite')
    cur = conn.cursor()
        # https://www.sqlite.org/lang_select.html
    sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

    for row in cur.execute(sqlstr):
        print(str(row[0]), row[1])

    cur.close()

    out, err = capfd.readouterr()
    assert "iupui.edu 536" in out
    assert "umich.edu 491" in out
    assert "indiana.edu 178" in out
    assert "caret.cam.ac.uk 157" in out
    assert "vt.edu 110" in out
    assert "uct.ac.za 96" in out
    assert "media.berkeley.edu 56" in out
    assert "ufp.pt 28" in out
    assert "gmail.com 25" in out
    assert "et.gatech.edu 17" in out

