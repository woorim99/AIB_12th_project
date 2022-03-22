PUBG Finish Placement Prediction
=============
* 데이터 출처: https://www.kaggle.com/c/pubg-finish-placement-prediction/data

> target = 'winPlacePerc'(상위 10%면 1, 아니면 0)

> features = ['boosts', 'damageDealt', 'heals', 'killPlace','kills', 'matchDuration', 'maxPlace', 'roadKills', 'vehicleDestroys', 'weaponsAcquired', 'totalDistance', 'headshotKillsPerKills', 'useCar']

Timeline
-------------
### 22.03.17
* 데이터 불러오기
* 결측치 삭제
* 불필요한 row, column 삭제
* 매치 종류 별 시각화

### 22.03.18
* train/test/validation 데이터 split
* 새로운 column 추가
* 전처리 완료 및 전처리 과정 함수로 변경

### 22.03.21
* 모델 학습
* 모델 정확도 올리기
* 모델 해석

### 22.03.22
* 부족한 부분 보충
* 피피티 작성
* 발표 영상 촬영
