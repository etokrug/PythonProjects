"""
Email message handling module: contains logic
to store email using a MySQL relational database.
"""

from database import login_info
import mysql.connector as msc
from email import message_from_string

conn = msc.Connect(**login_info)
curs = conn.cursor()

def  store(msg):
    """
    stores an email message, if necessary, returning its primary key
    """
    message_id = msg['message-id']
    text = msg.as_string()
    curs.execute("select msgID from message where msgMessageID=%s", (message_id, ))
    result = curs.fetchone()
    if result:
        return result[0]
    curs.execute("insert into message (msgMessageID, msgText) values (%s, %s)", (message_id, text))
    conn.commit()
    curs.execute("select msgID from message where msgMessageID=%s", (message_id, ))
    return curs.fetchone()[0]