import unittest
import mysql.connector as msc
from database import login_info
from jotd import createMessages, getRandomJoke
from jokes import jokes
from settings import recipients, startDate, daycount

conn = msc.Connect(**login_info)
curs = conn.cursor()


emailTable= """\
create table jMessage (
    msgID integer auto_increment primary key,
    msgMessageID varchar(128),
    msgDate datetime,
    msgSenderName varchar(128),
    msgSenderAddress varchar(128),
    msgRecipientName varchar(128),
    msgRecipientAddress varchar(128),
    msgText longtext
)"""

jotdTable = """\
create table jotd (
    jotdID integer auto_increment primary key,
    joke longtext
)"""

class testJotd(unittest.TestCase):
    def setUp(self):
        """
        Creates jotd table if does not exist.
        Creates jMessage table if does not exist.
        Inserts data into jotd table from jokes
        """
        curs.execute("drop table if exists jMessage;")
        curs.execute("drop table if exists jotd;")
        curs.execute(emailTable)
        curs.execute(jotdTable)
        for j in jokes:
            curs.execute("insert into jotd (joke) values ( %s );", (j, ))
        
    def testJotdNotEmpty(self):
        """
        Check that the jotd table is not empty
        """
        curs.execute("select count(*) from jotd;")
        messageCt = curs.fetchone()[0]
        self.assertGreater(messageCt, 0, "jotd Table is empty")
    
    def testTotalMessages(self):
        """
        Check that the messages generated is equal the the amount of recipients.
        Calls the createMessages function in the jotd.py module
        """
        recpCt = len(recipients)
        daysOut = int(daycount.days)
        totEmails = recpCt * daysOut
        createMessages(recipients, startDate, daycount)
        curs.execute("select count(*) from jMessage;")
        realEmailCt = curs.fetchone()[0]
        self.assertEqual(totEmails, realEmailCt, "Email counts are inconsistent.")
    
    def testRandomJoke(self):
        """
        Tests that the joke which was randomly pulled is in the database
        """
        fullJokeList = []
        curs.execute("select joke from jotd;")
        for jokeTuple in curs.fetchall():
            fullJokeList.append(jokeTuple[0])
        jokeText = getRandomJoke()
        self.assertIn(jokeText, fullJokeList, "Joke was not found in database")





if __name__=="__main__":
    unittest.main()
        