#!/usr/bin/python
# This script allows you to send a file to a given notebook in Evernote. 
#
# Author: Luca Zorzi (@LucaTNT)
# Version: 0.1
# License: BSD
# ----------------------------------
# Usage: sendToEvernote.py NOTEBOOK ATTACHMENT_PATH [NOTE_TITLE] [NOTE_TEXT]

import sys, os, pkgutil

# Settings, MAKE SURE YOU EDIT THESE!
SMTP_SERVER = "" # Your ISP's SMTP server
SMTP_PORT = 25
FROM_ADDRESS = "" # The email you used to register to Evernote
TO_ADDRESS = "" # The email Evernote assigned to you. You can find it in the 'Account Info' section of the Evernote app.



if len(sys.argv) < 3:
	print "ERROR: You must specify at least a notebook and the path of the attachment\n"
	print "Usage: sendToEvernote.py NOTEBOOK ATTACHMENT_PATH [NOTE_TITLE] [NOTE_TEXT]"
	sys.exit(5)


NOTEBOOK = sys.argv[1]
ATTACHMENT_FILE = sys.argv[2]

if not os.path.isfile(ATTACHMENT_FILE):
	print "ERROR: The attachment file could not be found."
	sys.exit(6)

NOTE_TITLE = os.path.basename(ATTACHMENT_FILE)
# Set the proper note title if it is specified
if len(sys.argv) > 3:
	# Only accept the specified title if it is not empty
	if sys.argv[3]:
		NOTE_TITLE = sys.argv[3]

SUBJECT = NOTE_TITLE + " @" + NOTEBOOK

# Set the proper note text value if it is specified
if len(sys.argv) > 4:
	NOTE_TEXT = sys.argv[4]
else:
	NOTE_TEXT = ""


# Make sure that the required 'mailer' module is available
if "mailesr" in [tuple_[1] for tuple_ in pkgutil.iter_modules()]:
	from mailer import Mailer
	from mailer import Message

	# Create the message and attach the file
	message = Message(From=FROM_ADDRESS,
                  To=[TO_ADDRESS],
                  Subject=SUBJECT)
	message.Body = NOTE_TEXT
	message.attach(ATTACHMENT_FILE)

	# Send the message
	sender = Mailer(SMTP_SERVER, port=SMTP_PORT)
	sender.send(message)
else:
	print "ERROR: mailer module not found."
	print "On OS X and other *nix systems you can install it by running 'sudo easy_install mailer'"
	sys.exit(10)
