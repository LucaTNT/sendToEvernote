# sendToEvernote.py

## What is this thing?

sendToEvernote is a simple Python script I made in order to let me automate the process of sending files to my Evernote account.

I use it in conjunction with the great [Hazel](http://www.noodlesoft.com/hazel.php) app for Mac to enhance my paperless Workflow.

## How does it work?

It sends an email to your secret Evernote address, attaching the file and saving it to the desidered notebook.

You can find you secret address in the "Account Info" section of the Evernote app.

![Secret Evernote address](http://cl.ly/a5tO/Screen%20Shot%202015-03-06%20at%2013.15.06.png)

This script requires the `mailer` Python module. On many OSs, OS X included, you can install it by running:

    sudo easy_install mailer

If you don't have that module installed, sendToEvernote will complain. Be nice to sendToEvernote.

## Cool, how do I use it?

It's pretty simple. The *first* thing you have to do is to edit the settings at the top of the script. You have to enter:

 * Your ISP's SMTP server, in order to send e-mails to Evernote
 * The email associated with your Evernote account
 * Your Evernote secret address

Once you adjusted these settings, you're all set. Just launch the script.

    sendToEvernote.py NOTEBOOK ATTACHMENT_PATH [NOTE_TITLE] [NOTE_TEXT]

As you can see, there are 4 parameters, 2 of which are required.

 * `NOTEBOOK`, required: the notebook name.
 * `ATTACHMENT_PATH`, required: the file you wish to send to Evernote.
 * `NOTE_TITLE`, optional: you can set the note's title. If empty or not set it will default to the file name.
 * `NOTE_TEXT`, optional: the text of the note. Empty by default.

## That's great, but what about Hazel?

As I mentioned above, a great use case for this script is by invoking it through Hazel.

Say you have a rule that processes your invoices, and you want all of them sent to Evernote into your "Invoices" notebook. Easy:

![A sample Hazel rule to trigger sendToEvernote](http://cl.ly/a5a0/Screen%20Shot%202015-03-06%20at%2013.43.32.png)

Just a note: make sure the script is executable by running:

    chmod +x /path/to/sendToEvernote.py

## Awesome. But I think feature XYZ is still missing.

Fair enough. Drop me a line on Twitter, I'm [@LucaTNT](https://twitter.com/LucaTNT) there, I'll see what I can do.
