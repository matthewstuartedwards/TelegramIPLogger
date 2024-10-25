#!/usr/bin/env python

from telethon import TelegramClient
import subprocess
# Use your own values from my.telegram.org
api_id = 12345678
api_hash = 'ausldfkjuaslkdjfusalkdfjulsakjfd'


client = TelegramClient( 'IPLogger', api_id, api_hash )
hostname = subprocess.getoutput(["hostname"])
addresses = subprocess.getoutput(["hostname -I"])
addresses = addresses.replace( ' ', '\n')
async def main():
    #me = await client.get_me()
    #print( me.stringify())

    previousMessages = await client.get_messages( 'IPLogger', None)
    for x in previousMessages:
        await x.delete()

    await client.send_message('IPLogger', hostname, silent=True)
    await client.send_message('IPLogger', addresses, silent=True )


with client:
	client.loop.run_until_complete(main())

