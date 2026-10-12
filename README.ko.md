<a href="README.md">English README</a>

# VideoToPianoV2
```2025/11/13 ~```  
영상과 MIDI 파일을 입력하면 영상의 피치를 조절해서 뮤직비디오로 만들어 주는 프로그램 입니다.  

### 사용예시 (소리를 켜주세요)
처리전


https://github.com/user-attachments/assets/787c194f-cd08-49f6-b017-df560cd9bcd1


처리후


https://github.com/user-attachments/assets/d4c803f0-01f0-4ac7-8407-ac6f1294efee


처리전


https://github.com/user-attachments/assets/a15dc16a-c64b-482c-8888-8583f693bc83


처리후


https://github.com/user-attachments/assets/8c8f985f-fefc-40eb-a5d3-8c13498bbea0



### 준비물
1. 1:1 비율의 .mp4 영상
2. MIDI 파일

### 사용방법
파이썬 3.13 이하의 버전이 설치되어있어야 합니다.

#### 초기설정
1. ```git clone https://github.com/SeunggyuKwak/VideoToPianoV2``` 또는 릴리즈에서 ```Source code.zip``` 다운로드
2. ```pip install -r requirements.txt```

#### 영상 처리
1. ```/inst``` 에 원하는 이름의 폴더를 생성
2.  ```/inst/{원하는 폴더명}``` 에 ```original.mp4``` 로 원하는 영상 저장
3. ```VideoProsessor.py``` 실행 후 처리할 폴더의 번호 입력

* 한 영상에 대해 한번만 실행하면 됩니다. (제작할때마다 영상처리를 다시 할 필요 없음)

#### MIDI 파일 저장
1. ```/midi``` 에 원하는 MIDI 파일 저장 (.mid .midi)

#### 영상 제작
1. ```Player.py``` 실행
2. 파일 선택창에서 원하는 MIDI(.mid/.midi)파일 선택
3. 원하는 영상폴더 이름의 번호 입력
4. ```/output/{선택한 폴더명}``` 에서 완성된 영상 확인

### 개선할 점
- 영상의 음계를 자동으로 측정하는 기능을 추가해 더 정확한 음을 재생할수 있도록 한다.
- 음의 크기(볼륨)를 고려하여 처리하는 기능을 추가한다.
- 한 영상에서 여러 악기를 사용할수 있도록 악기의 종류(드럼, 베이스, 피아노 등)를 다양하게 선택할수 있는 기능을 추가한다.