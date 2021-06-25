import time
import requests
import json


token = "PUT-HERE-YOUR-DISCORD-TOKEN"
headers = {"Authorization": token, "Content-Type": "application/json"}
url = "https://discordapp.com/api/users/@me/settings"

stuffs = ["This", "changes", "every", "3", "seconds"]

while True:
  for stuff in stuffs: 
    status_data = json.dumps({
        "custom_status": {
          "text": stuff,
          "emoji_name": "😊" # Here you can put any emoji you want
        }
      })

    r = requests.patch(url, headers=headers, data=status_data)
    
    time.sleep(3) # Important!! The minimun time must be 3 seconds or you will be sending lot of requests to the discord api and you could get banned :l
