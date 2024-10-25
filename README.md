# TelegramIPLogger
Logs your computer's IP addresses so you can find it later.  Useful for telecommuting if you don't have a DNS entry at the remote location.
Sends all IP addresses on your computer using the iplogger username. Deletes all messages from that user before adding more to prevent the message log from getting very large.


#Setup:

Follow the Telethon documentation for Signing In: https://docs.telethon.dev/en/stable/basic/signing-in.html
Obtain an api_id and api_hash.  Replace those values in the logIPToTelegram.py file.

Run the script with `python logIPToTelegram.py`.  The first time you run it, you will be asked to enter your phone number and then the code received.  After that you'll need to enter your Telegram password.  After that you will have successfully signed in and a .session file will be created.  If this session file is removed you'll have to manually log in again which means automatically running the script will stop working.

#Running the script automatically:
On linux, modify the `addCronJob.sh` file to point to where you downloaded the logIPToTelegram.py file and then run the file (or just copy the one line and run it).  This will add a cron job that will run the script every day at 6am.  You can modify the cron job parameters to suit your level of automation.

