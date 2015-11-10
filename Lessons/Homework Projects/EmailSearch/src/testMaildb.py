"""
read in and parse email messages to verify readability.

Note: this test creates the message table, dropping any
previous version and should leave it empty. Danger:
this test will delete any existing message table.
"""

from glob import glob
from email import message_from_string
import mysql.connector as msc
from database import login_info
import maildb
import unittest
import shutil
import os

conn = msc.Connect(**login_info)
curs = conn.cursor()

TBLDEF = """\
create table message (
    msgID integer auto_increment primary key,
    msgMessageID varchar(128),
    msgText longtext
)"""
FILESPEC = "C:/PythonData/*.eml"

class testRealEmail_traffic(unittest.TestCase):
    def setUp(self):
        """
        reads an arbitrary number of mail messages and
        stores them in a brand new messages table.
        
        Danger: any existing message table will be lost.
        """
        curs.execute("drop table if exists message")
        conn.commit()
        curs.execute(TBLDEF)
        conn.commit()
        files = glob(FILESPEC)
        self.msgids = {} #Keyed by message_id
        self.message_ids = {} # keyed by id
        for f in files:
            srcfile = os.path.abspath(f)
            print(srcfile)
            shutil.copy(srcfile, 'V:\\workspace')
            ff = open(f)
            text = ff.read()
            msg = message_from_string(text)
            id = self.msgids[msg['message-id']] = maildb.store(msg)
            self.message_ids[id] = msg['message-id']
        
    def test_not_empty(self):
        """
        verify that the setUp method actually created some messages.
        if it finds no files there will be no messages in the table,
        the loob bodies in the other tests will never run, and potential
        errors will never be discovered
        """
        curs.execute("select count(*) from message")
        messagect = curs.fetchone()[0]
        self.assertGreater(messagect, 0, "Database message table is empty")
    
    def test_message_ids(self):
        """
        verify that items retrieved by id have the correct Message-ID.
        """
        for message_id in self.msgids.keys():
            pk, msg = maildb.msg_by_id(self.msgids[message_id])
            self.assertEqual(msg['message-id'], message_id)
    
    def test_ids(self):
        """
        verify that items retrieved by message_id have the correct Message-ID
        """
        for id in self.message_ids.keys():
            pk, msg = maildb.msg_by_message_id(self.message_ids[id])
            self.assertEqual(msg['message-id'], self.message_ids[id])

if __name__ == '__main__':
    unittest.main()
            