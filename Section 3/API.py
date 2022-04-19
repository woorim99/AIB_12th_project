import requests 

header = { 
    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIyN2UxN2U4MC1hMTA5LTAxM2EtYzQ5OS0wZTVmZGQ2ODc3NTYiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjUwMjYwOTM0LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6Indvb19wMyJ9.9ee6mVz2tpkFlzb1P6QccxB3DwVHHa3DPu1zve4y690", 
    "Accept": "application/vnd.api+json" 
    }

name = 'S2_Rimi'
# id = "account.cacb55280bb84012bc04ac2999f76fee"
woorim_url = "https://api.pubg.com/shards/kakao/players?filter[playerNames]=S2_Rimi"  #유저정보

woorim_r = requests.get(woorim_url, headers=header)

player_woorim_json = woorim_r.json()

id = player_woorim_json['data'][0]['id']

survival_url = f"https://api.pubg.com/shards/kakao/players/{id}/survival_mastery"  #딜평균 총량 등등
weapon_url = f"https://api.pubg.com/shards/kakao/players/{id}/weapon_mastery"     #무기 마스터리
weapon_r = requests.get(weapon_url, headers=header)




survival_r = requests.get(survival_url, headers=header)

survival_json = survival_r.json()
weapon_json = weapon_r.json()

# print(survival_json)
print(survival_json['data']['attributes']['stats']['damageDealt']['average'])
print(survival_json['data']['attributes']['stats']['damageDealt']['average']//100)
print(survival_json['data']['attributes']['stats']['distanceTotal']['average'])