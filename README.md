# Telethon_glish
Extract messages from a public channel Telegram / Extraire les messages d’un canal Telegram public

#### Un outil Python simple basé sur la bibliothèque Telethon pour :

✅ Se connecter à l’API Telegram
✅ Extraire les messages d’un canal public
✅ Sauvegarder les messages dans un fichier .txt ou .csv

* 📦 Étape 1 – Installer Telethon
```bash
pip install telethon
```
* 🛠️ Étape 2 – Créer une app Telegram pour obtenir tes clés API

Lien => <a href="https://my.telegram.org">https://my.telegram.org</a>

* Connecte-toi avec ton numéro
* Clique sur API Development Tools
* Remplis les champs → Tu obtiendras un api_id et un api_hash

* 🐍 Étape 3 – Script Python (extraction simple)
```python
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
```
✅ Résultat

=> Tu obtiendras un fichier messages.txt contenant les 100 derniers messages du canal public.

