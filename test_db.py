import mock
import pytest

from emaildb import print_counts_of_emails_from_file


def test_long_mbox(capfd):
    with mock.patch('builtins.input', side_effect=['']):
        print_counts_of_emails_from_file()

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

