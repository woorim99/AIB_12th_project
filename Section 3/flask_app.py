from flask import Flask, render_template, request
import pickle
import numpy as np
import requests 

model = pickle.load(open('pubg.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def home():
    name = request.form['name']
    header = { 
    "Authorization": "API key", 
    "Accept": "application/vnd.api+json" 
    }

    player_url = f"https://api.pubg.com/shards/kakao/players?filter[playerNames]={name}"  #유저정보

    player_r = requests.get(player_url, headers=header)

    player_json = player_r.json()

    id = player_json['data'][0]['id']   #유저닉네임을 통해 유저 고유 id 받아오기

    survival_url = f"https://api.pubg.com/shards/kakao/players/{id}/survival_mastery"  #딜평균 이동거리 평균 등등 등등

    survival_r = requests.get(survival_url, headers=header)

    survival_json = survival_r.json()
    
    #유저의 딜평균, 킬평균, 이동거리 평균 구하기(킬 평균은 안나와 있어서 딜평균을 100으로 나눈 몫으로 설정)
    damageDealt = survival_json['data']['attributes']['stats']['damageDealt']['average']    
    kills = damageDealt//100
    totalDistance = survival_json['data']['attributes']['stats']['distanceTotal']['average']
    
    arr = np.array([[damageDealt, kills, totalDistance]])
    
    pred = model.predict(arr)
    return render_template('predict.html',name=name, data=pred, damageDealt=int(damageDealt//1), kills=int(kills//1), totalDistance=int(totalDistance//1))

if __name__ == "__main__":
    app.run(debug=True)