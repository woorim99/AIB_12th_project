# API를 통해 가져온 데이터를 data.db에 저장합니다.

import requests
import sqlite3

header = { 
    "Authorization": "API key", 
    "Accept": "application/vnd.api+json" 
    }

#player라는 닉네임의 유저가 최근 14일 내에 플레이 한 매치들을 리스트 형태로 반환
def returnPlayerMatch(player):    
    url = f"https://api.pubg.com/shards/kakao/players?filter[playerNames]={player}"
    r = requests.get(url, headers=header)
    player_json = r.json()
    
    match_list = []
    for i in player_json['data'][0]['relationships']['matches']['data']:
        match_list.append(i['id'])
        
    return match_list


# match_list안의 매치 속 플레이어들의 스탯 data.db의 pubg_stat에 저장
def returnUserStat(match_list):
    user_stat = []
    id = 0
    for matchId in match_list:
        match_url = f"https://api.pubg.com/shards/kakao/matches/{matchId}"
        match_r = requests.get(match_url, headers=header)
        match_json = match_r.json()
        
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        
        for i in match_json['included']:       
            try: 
                user_stat.append(i['attributes']['stats'])
                kills = i['attributes']['stats']['kills']
                damageDealt = i['attributes']['stats']['damageDealt']
                totalDistance = i['attributes']['stats']['rideDistance'] + i['attributes']['stats']['swimDistance'] + i['attributes']['stats']['walkDistance']
                winPlace = i['attributes']['stats']['winPlace']
                
                cur.execute(f"INSERT INTO pubg_stat VALUES ({id}, {kills}, {damageDealt}, {totalDistance}, {winPlace})")
                id += 1
            except:
                pass
            conn.commit()
    return(id)  

match_list = returnPlayerMatch('플레이어 닉네임')  #플레이어 닉네임에 원하는 플레이어 이름 작성
print(returnUserStat(match_list))

