import os
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

def emailReturn(eAddress, eBody, eAttach):
    msg = MIMEMultipart()
    msg['To'] = eAddress
    msgBody = MIMEText(eBody)
    msg.attach(msgBody)

    for attachment in eAttach:
        
        #test if it is an 
        mimeMainType = mimetypes.guess_type(attachment)[0].split('/')[0]
        mimeSubType = mimetypes.guess_type(attachment)[0].split('/')[1]
        if  mimeMainType == 'image':
            imgAttachment = open(attachment, 'rb')
            img = MIMEImage(imgAttachment.read())
            imgAttachment.close()
            img.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachment))
            msg.attach(img)
        elif mimeMainType == 'text':
            if mimeSubType == 'plain':
                plainText = MIMEText(attachment, 'plain')
                msg.attach(plainText)
            if mimeSubType == 'html':
                htmlText = MIMEText(attachment, 'html')
                msg.attach(htmlText)
    return msg