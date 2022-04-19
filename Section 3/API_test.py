#test파일입니다.

import requests 

name = 'S2_Rimi'
id = "account.cacb55280bb84012bc04ac2999f76fee"
woorim_url = "https://api.pubg.com/shards/kakao/players?filter[playerNames]=S2_Rimi"  #유저정보
match_url = "https://api.pubg.com/shards/kakao/matches/968ae5a2-f75c-489e-88d8-19c4de609456"   #매치정보
weapon_url = f"https://api.pubg.com/shards/kakao/players/{id}/weapon_mastery"     #무기 마스터리
survival_url = f"https://api.pubg.com/shards/kakao/players/{id}/survival_mastery"  #딜평균 총량 등등
lifetime_url = f"https://api.pubg.com/shards/kakao/players/{id}/seasons/lifetime?filter[gamepad]=false"         #매치타입별 생존시간

header = { 
    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIyN2UxN2U4MC1hMTA5LTAxM2EtYzQ5OS0wZTVmZGQ2ODc3NTYiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjUwMjYwOTM0LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6Indvb19wMyJ9.9ee6mVz2tpkFlzb1P6QccxB3DwVHHa3DPu1zve4y690", 
    "Accept": "application/vnd.api+json" 
    }



woorim_r = requests.get(woorim_url, headers=header)
match_r = requests.get(match_url, headers=header)
weapon_r = requests.get(weapon_url, headers=header)
lifetime_r = requests.get(lifetime_url, headers=header)
survival_r = requests.get(survival_url, headers=header)

player_woorim_json = woorim_r.json()
match_json = match_r.json()
weapon_json = weapon_r.json()
survival_json = survival_r.json()
lifetime_json = lifetime_r.json()

print(player_woorim_json['data'][0]['id'])
# print(match_json)
# print(weapon_json)
# print(survival_json)
# print(lifetime_json)