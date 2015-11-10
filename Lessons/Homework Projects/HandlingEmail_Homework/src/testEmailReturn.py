import unittest
import os
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

from emailReturnModule import emailReturn


class emailStringTest(unittest.TestCase):
    
    def setUp(self):
        
        #set up the image for the message
        ePic = 'v:/workspace/HandlingEmail_Homework/src/python-logo.png'
        att = open(ePic, 'rb')
        img = MIMEImage(att.read())
        att.close()
        img.add_header('Content-Disposition', 'attachment', filename=os.path.basename(ePic))
        
        #set up the message body
        msgText = MIMEText("This is a test string", 'plain')
        
        #build the message
        msg = MIMEMultipart()
        msg['To'] = 'etokrug@yahoo.com'
        msg['From'] = 'etokrug@yahoo.com'
        msg['Subject'] = 'Test Email'
        msg.attach(msgText)
        msg.attach(img)
        self.Mmsg = msg
        
        #create a set for comparison
        self.attachmentSet = {msgText.as_string(), img.as_string()}
        
        #engages the function
        attachments = [ePic]
        mailObj = emailReturn('etokrug@yahoo.com', 'This is a test string', attachments)
        self.mailTest = mailObj

    def test_eAddress(self):
        self.assertEqual(self.Mmsg['To'], self.mailTest['To'])
    
    def test_eBody(self):
        
        mailTestSet = set()
        for attachment in self.mailTest.get_payload():
            mailTestSet.add(attachment.as_string())
        
        self.assertEqual(self.attachmentSet, mailTestSet)

if __name__ == "__main__":
    unittest.main()