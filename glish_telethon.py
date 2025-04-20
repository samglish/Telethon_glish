from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest

# Remplace ces infos par les tiennes
api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'
username = 'session_samuel'

# Nom d'utilisateur ou lien du canal (ex: 'cybersec_cameroon')
target_channel = 't.me/nom_du_canal'  # ou juste 'nom_du_canal'

with TelegramClient(username, api_id, api_hash) as client:
    entity = client.get_entity(target_channel)
    messages = client(GetHistoryRequest(
        peer=entity,
        limit=100,  # nombre de messages à extraire
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0,
        hash=0
    ))

    with open("messages.txt", "w", encoding="utf-8") as f:
        for message in messages.messages:
            if message.message:  # si le message est du texte
                f.write(f"{message.date} - {message.message}\n\n")
