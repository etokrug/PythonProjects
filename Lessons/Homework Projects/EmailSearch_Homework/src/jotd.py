import datetime
from email import message_from_string
from email.utils import make_msgid
from database import login_info
import mysql.connector as msc
from random import randint

conn = msc.Connect(**login_info)
curs = conn.cursor()

randomJokeIdSet = set()
randomJokeIdList = []

def getRandomJoke():
    curs.execute("select jotdId from jotd;")
    for jotdId in curs.fetchall():
        randomJokeIdList.append(jotdId)
    if len(randomJokeIdSet) == 50:
        randomJokeIdSet.clear()
    while True:
        try:
            randJokeIndex = randint(1, len(randomJokeIdList))
            if randomJokeIdList[randJokeIndex] in randomJokeIdSet:
                continue
            else:
                randomJokeIdSet.add(randJokeIndex)
                break
        except IndexError:
            continue
    jokeId = randomJokeIdList[randJokeIndex]
    curs.execute("select joke from jotd where jotdID=%s;", (jokeId))
    jokeText = curs.fetchone()[0]
    return jokeText

def createMessages(toList, beginOn, totalDays):
    """
    Creates emails to all recipients in the toList from an email
    randomly pulled from the database
    toList = a list of (email, name) tuples
    beginOn = a datetime object
    totalDays = a timedelta object
    """
    senderName = 'Spamguy31415'
    senderAddress = 'spammailguy31415@spammail.com'
    jDayCount = int(totalDays.days)
    for day in range(jDayCount):
        joke = getRandomJoke()
        for nameTup in toList:
            em, nm = nameTup
            jotdMail = """Hello {0},\n
            Please see my famous JOTD:\n
            {1}\n
            Thank you,\n
            -Spambot""".format(nm, joke)
            msg = message_from_string(jotdMail)
            date = beginOn + datetime.timedelta(day)
            msg['Date'] = date.strftime('%m/%d/%Y %H:%M:%S')
            msg['From'] = 'spammailguy31415@spammail.com'
            msg['To'] = em
            msg['Message-Id'] = make_msgid()
            msgAsString = msg.as_string()
            curs.execute("insert into jMessage (msgMessageID, msgDate, msgSenderName, msgSenderAddress, msgRecipientname, msgRecipientAddress, msgText) values (%s, %s, %s, %s, %s, %s, %s);", 
            (msg['Message-Id'], date, senderName, senderAddress, nm, em, msgAsString))
            
            
            
            
            
            
            
            
            