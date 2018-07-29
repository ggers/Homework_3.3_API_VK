
import requests

def get_mutual_VKfriends(VK_token, uid2):
    response = requests.get("https://api.vk.com/method/friends.getMutual",
                            params=dict(access_token=VK_token, v=5.80, target_uid=uid2))
    return response.json()

VK_token = input("Введите необходимый токен доступа для первого пользователя\n")
uid2 = input("Введите идентификатор второго пользователя\n")

#запускаем функцию с заранее прописанным токеном, так как не уверен, что его можно адекватно передать черех Input()
json_list = get_mutual_VKfriends("4b62d22e2ae7da0328dddf3232fa7caf418080c6495806c4217106c6b54e961dfefca532923fe72fd7016", uid2)
for user_id in json_list["response"]:
    print(f"Общий друг с идентификатором {user_id}, ссылка на страницу: https://vk.com/id{user_id}")
