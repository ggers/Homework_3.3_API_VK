from urllib.parse import urlencode

APP_ID = "7777777"
AUTH_SERVER = "https://oauth.vk.com/authorize"
auth_data = {
    "client_id": APP_ID,
    "display": "page",
    "redirect_url": "https://oauth.vk.com/blank.html",
    "scope": "status,friends",
    "response_type": "token",
    "v": 5.80
}

TOKEN = "XXX"