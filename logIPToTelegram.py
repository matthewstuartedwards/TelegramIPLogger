from telethon import TelegramClient
import subprocess
# Use your own values from my.telegram.org
api_id = 12345678
api_hash = 'ausldfkjuaslkdjfusalkdfjulsakjfd'


client = TelegramClient( 'IPLogger', api_id, api_hash )
hostname = subprocess.getoutput(["hostname"])
addresses = subprocess.getoutput(["hostname -I"])

async def main():
    me = await client.get_me()
    print( me.stringify())

    await client.send_message('IPLogger', hostname)
    await client.send_message('IPLogger', addresses )


with client:
	client.loop.run_until_complete(main())

