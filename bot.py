from telethon.sync import TelegramClient, events
import api_data
with TelegramClient('name',api_data.api_id, api_data.api_hash) as client:
    #client.send_message('me', 'Hello, myself!')
    #print(client.download_profile_photo('me'))

    @client.on(events.NewMessage(chats=api_data.admin_username))
    async def handler(event):
       sender = await event.get_sender()
       if sender.bot:
           await event.reply('Usted es un bot.')
        
    client.run_until_disconnected()


#from telethon.sync import TelegramClient
#import re
#from telethon import events
#import api_data

#client = TelegramClient('sesion', api_data.api_id, api_data.api_hash)

#@client.on(events.NewMessage(chats=api_data.admin_username))
#async def handle_new_message(event):
#    sender = await event.get_sender()
#    message = event.message.message.lower()
#    if sender.bot:
#        await event.reply('Usted es un bot.')
#    elif re.search(r'\bhi\b', message):
#        await event.reply('¡Hola! ¿Cómo puedo ayudarte?')

# Iniciar el cliente de Telethon
#if __name__ == '__main__':
#    client.run_until_disconnected()





