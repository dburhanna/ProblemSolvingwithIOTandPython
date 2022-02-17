
# this worked too!

import smtplib

# Establish a secure session with gmail's outgoing SMTP server using your gmail account
server = smtplib.SMTP( "smtp.gmail.com", 587 )

server.starttls()

server.login( 'burhanna.douglas@hermits.com', 'BaDs1959*928' )

# Send text message through SMS gateway of destination number
server.sendmail( 'burhanna.douglas@hermits.com', '6098278557@txt.att.net', 'Sending you a text from python' )
