[CodeStates Project] SNS 관광리뷰 데이터 NLP(자연어) 처리 분석
===

![01](https://github.com/Sanghoon-Oh-34/cs_project04/blob/master/2.%20Slides/01.jpg)

## 개요
* 코드스테이츠 AI 부트캠프에서 진행한 NLP(자연어) 처리 프로젝트입니다.
* 목적: 관광리뷰 텍스트 분석을 통해 경지 지역 관광지의 현황과 개선방안 도출
* 데이터셋: 경기지역경제포털 SNS 관광객 리뷰 웹문서 데이터 14,836건

## 내용
1. 데이터 소개 및 선정 이유  

 <img src='https://github.com/Sanghoon-Oh-34/cs_project04/blob/master/2.%20Slides/04.jpg' width='400px' height='300px'></img>
 <img src='https://github.com/Sanghoon-Oh-34/cs_project04/blob/master/2.%20Slides/05.jpg' width='400px' height='300px'></img>
* 트립어드바이저에서 수집한 다양한 언어로 작성된 관광객 리뷰 데이터
* 세상의 대부분 정보는 텍스트로 이루어져 있어 자연어 처리에 대한 관심
* 경기도민, 여행을 좋아하는 개인적인 이유로 선정

<br>

2. 데이터 전처리  

<img src='https://github.com/Sanghoon-Oh-34/cs_project04/blob/master/2.%20Slides/07.jpg' width='400px' height='300px'></img>
<img src='https://github.com/Sanghoon-Oh-34/cs_project04/blob/master/2.%20Slides/08.jpg' width='400px' height='300px'></img>
* 각 나라 언어로 작성된 데이터에서 정규표현식을 이용하여 한글 리뷰만 추출
* 특수문자 및 숫자를 공백으로 치환
* 관광지별 그룹화하여 개별적으로 작성된 리뷰 데이터 결합
<br>

3. 토큰화

<img src='https://github.com/Sanghoon-Oh-34/cs_project04/blob/master/2.%20Slides/12.jpg' width='400px' height='300px'></img>
<img src='https://github.com/Sanghoon-Oh-34/cs_project04/blob/master/2.%20Slides/13.jpg' width='400px' height='300px'></img>
* 한국어 특성 상 어절 토큰화가 아닌 형태소 토큰화 진행
* KoNlpy(코엔엘파이) - Twitter(Okt) 오픈 소스 한글 형태소 분석기 사용
* 불용어 사전 자체 제작하여 1~3차까지 불용어 처리

<br>

4. 분석 및 결과  

<img src='https://github.com/Sanghoon-Oh-34/cs_project04/blob/master/2.%20Slides/16.jpg' width='400px' height='300px'></img>
<img src='https://github.com/Sanghoon-Oh-34/cs_project04/blob/master/2.%20Slides/17.jpg' width='400px' height='300px'></img>
* 상위 빈도수 단어: '좋은', '방문', '공원', '아이', '산책', '가족'
  - 긍정적 평가 다수, 가족 단위(아이 동반) 방문객, 공원과 산책에 대한 관심도 높음
* 상위 관광지의 경우 대부분 아이가 있는 가족 단위 관광지에 특성화 되어 있음
* 하위 관광지의 경우 타 관광지에 비해 개인 취향을 강하게 타는 장소/컨셉을 가짐
  - 경기 지역 관광지 활성화 중점 키워드는 '가족 단위', '자연', '교육용' 테마 개발 필요

<br>

5. 회고  

<img src='https://github.com/Sanghoon-Oh-34/cs_project04/blob/master/2.%20Slides/22.jpg' width='400px' height='300px'></img>
* 데이터 정제에 대한 지속적인 학습 필요
* 단순 데이터 분석한 결과만 바라보는게 아닌 그 이후 어떤 행동을 취해야 할지 Action 대안 제시
