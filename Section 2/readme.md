PUBG Finish Placement Prediction
=============
* 데이터 출처: https://www.kaggle.com/c/pubg-finish-placement-prediction/data

> target = 'winPlacePerc'(상위 10%면 1, 아니면 0)

> features = ['boosts', 'damageDealt', 'heals', 'killPlace','kills', 'matchDuration', 'maxPlace', 'roadKills', 'vehicleDestroys', 'weaponsAcquired', 'totalDistance', 'headshotKillsPerKills', 'useCar']

Column 설명
-------------
#### 기존 columns
* DBNOs - 기절시킨 적 플레이어의 수
* assists - 이 플레이어가 피해를 입히고 팀 동료에 의해 사망한 플레이어의 수
* boosts - 사용한 부스팅 아이템의 수
* damageDealt - 팀킬 제외한 총 피해량
* headshotKills - 헤드샷으로 사망한 적 플레이어의 수
* heals - 사용한 치유 아이템의 수
* Id - 플레이어의 아이디
* killPlace - 이 매치의 킬 순위
* killPoints - 킬 수만의 외부 랭킹
* killStreaks - 단기간에 죽은 적의 최대 수
* kills - 죽인 적 플레이어의 수
* longestKill - 사망 시 사망한 플레이어와의 최장 거리
* matchDuration - 매치 시간
* matchId - 매치를 식별하는 아이디
* matchType - 게임모드를 식별(solo, duo, squad, solo-fpp, duo-fpp, squad-fpp 등)
* rankPoints - 플레이어의 Elo 랭킹
* revives - 팀원들을 소생시킨 횟수
* rideDistance - 차량으로 이동한 총 이동 거리(m 단위)
* roadKills - 차에 타고 있을 때의 킬 수
* swimDistance - 수영으로 이동한 총 이동거리(m 단위)
* teamKills - 팀원을 죽인 횟수
* vehicleDestroys - 차량은 파괴한 횟수
* walkDistance - 걸어서 이동한 총 이동 거리(m 단위)
* weaponsAcquired - 획득한 무기의 수
* winPoints - 순위로만 매겨진 랭킹
* groupId - 매치내 그룹을 식별하는 ID
* numGroups - 매치 안에 데이터가 있는 그룹의 수
* maxPlace - 매치 안에서의 제일 마지막 순위
* winPlacePerc - 예측의 타겟으로 순위 백분위 -> 상위 10%안에 들면 1, 상위 10%안에 들지 못하면 0)

#### 생성한 Columns
* totalDistance - 총 이동 거리(m 단위)
* headshotKillsPerkills - 킬 중에서 헤드샷 킬의 비율(킬이 없으면 -1)
* useCar - 차를 사용했으면 1, 차를 사용하지 않았으면 0

모델링
-------------
#### Decision Tree
* 검증데이터 정확도: 0.9248858483068149
* 검증데이터 precision:  0.6543557469360716
* 검증데이터 recall:  0.5911131059245961
* 검증데이터 f1_score: 0.6211287533406697
*![image](https://user-images.githubusercontent.com/64140376/188830725-f9b9b6e5-1288-4d94-b2f9-6acb50194977.png)

### Random Forest
* 검증데이터 정확도: 0.9369009958079446
* 검증데이터 precision:  0.731750219876869
* 검증데이터 recall:  0.6223818073010173
* 검증데이터 f1_score: 0.672649365348856
![image](https://user-images.githubusercontent.com/64140376/188830989-fd570db0-6ed9-4596-9d09-b6955718013e.png)


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
