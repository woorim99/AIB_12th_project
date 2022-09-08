PUBG TOP10 예측 웹 애플리케이션
=============
* 데이터 출처: https://developer.pubg.com/
1. PUBG API 이용하여 아이디 검색해서 TOP10 안에 들 수 있는 실력인지 확인

Data Pipeline
-------------
![image](https://user-images.githubusercontent.com/64140376/189045170-4c8cc690-ca8b-4e20-89fe-be1971886055.png)
1. PUBG DEVELOPER API에서 4명의 유저들이 최근 14일 내에 플레이한 매치 내의 모든 플레이어들의 데이터를 가져와서 SQLite에 저장
2. 랜덤포레스트로 모델링
3. 모델을 Flask에서 받아와 닉네임을 입력하면 API에서 그 닉네임을 가진 플레이어의 정보를 가져와 프론트 엔드에 결과 값을 나타냄.

결과
-------------
### 1. 메인페이지
![image](https://user-images.githubusercontent.com/64140376/189045898-7df7cdde-3d27-48bd-b8df-bf5fe17d0420.png)
### 2. TOP10 불가능 예측
![image](https://user-images.githubusercontent.com/64140376/189046006-529f95c3-caf1-4215-83f2-17c4afbf3e9e.png)
### 3. TOP10 가능 예측
![image](https://user-images.githubusercontent.com/64140376/189046056-8c092782-9a67-456b-9244-5d3785575e7d.png)


Timeline
-------------
### 22.04.18
* 데이터 결정
* PUBG API 실습
* 어떤 식으로 학습할 지 결정
   > * 여러 매치안에서 유저들의 스탯을 가져와 TOP10안에 드는지 안드는지 예측
   > * 아이디 검색을 통한 유저의 평균 딜량, 평균 킬, 평균 이동거리를 통해 TOP10안에 들 수 있는 실력인지 확인
* 데이터 DB에 저장

### 22.04.19
* DB에서 데이터 불러와 모델링
* Flask에 모델 불러오기
* Front-end 꾸미기

### 22.04.20
* Metabase Dashboard 제작

### 22.04.21
* 발표자료 만들기
* 발표영상 녹화
