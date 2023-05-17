# 앉은 자세 분류기

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Google Research의 MoveNet을 이용하여 생성한 데이터로 앉은 자세가 올바른지 아닌지 분류하기.

## Things to consider
- 일반화: 두 명의 사진이 들어갔지만, 더 많은 사람과 다양한 구도로 사진을 촬영해야 할 것
- 발표에 EDA 설명할 것. 웹캠 딜레이로 검은 화면이 나온 것, 일부 사진 발목 포인트 노이즈
- MoveNet은 사전학습된 모델로 어두운 화면이나 밝은 화면이나 큰 차이는 없어 보이지만, 다른 모델로 전처리하는 경우 환경 고려 필요
- 모델을 베포한다면 작은 하드웨어에 탑재해서 베포할 가능성 고려
- PC 사양 기재 및 실시간 감지 중 시간 출력 기능 추가
	+ `wait` 딜레이 수정 필요. `datetime`으로 처음시각 `+=`로 정확한 시간 추려보기
- 이상치 탐지 모델(train only normal sitting posture)로 접근해보는 것이 가장 좋은데, 여러 가지로 구성해보았지만 다 성능이 안 좋음.
	
## Credits
- Google Research for MoveNet
- TensorFlow for Movenet application