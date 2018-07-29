from urllib.parse import urlencode
import requests

APP_ID = "6646096"
AUTH_SERVER = "https://oauth.vk.com/authorize"
auth_data = {
    "client_id": APP_ID,
    "display": "page",
    "redirect_url": "https://oauth.vk.com/blank.html",
    "scope": "status,friends",
    "response_type": "token",
    "v": 5.80
}

id1 = 13575261
id2 = 343767


print("?".join((AUTH_SERVER, urlencode(auth_data))))

TOKEN = "4b62d22e2ae7da0328dddf3232fa7caf418080c6495806c4217106c6b54e961dfefca532923fe72fd7016"

response = requests.get("https://api.vk.com/method/friends.getMutual", params=dict(access_token=TOKEN, v=5.80, target_uid=id2))
print(response.text)


#Работа со статусами и получение токена
#response = requests.get("https://api.vk.com/method/status.get", params=dict(access_token=TOKEN, v=5.80))
#print(response.text)
#esponse = requests.get("https://api.vk.com/method/status.set", params=dict(access_token=TOKEN, v=5.80, text = "Проверка статуса"))
#https://oauth.vk.com/authorize?client_id=6646096&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends&response_type=token&v=5.52
#https://api.vk.com/method/users.get?user_id=13575261&v=5.52