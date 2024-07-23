## DARKNET 학습 설정

### 주요사항
- obj.data
    학습을 위한 내용이 담겨잇는 파일
    classes 개수, train,txt와 valid.txt의 경로, obj.names의 경로, weight를 저장할 폴더의 경로로 이루어짐
- obj.cfg
    모델 구조 및 train 과 관련된 설정이 들어잇는 파일
    batch 및 subdivisons 사이즈 (cuda memory 관련) width 및 height 사이즈
    augmentation(angle, saturation, exposure, hue)설정
    learning rate, burn-in, max-batches, policy, steps, scales 설정
    filter: (4 + 1 + class 수) * 3 설정
    classes: class 수 설정
    anchors 및 mask 설정
- weight file
    특정 미리 트레이님 된 모델 (pre-trained model) 또는 기본적으로 darknet53.conv.674등의 가중치 파일
    fine-tuning을 위해 맨 아래 레이어를 제거 (AlexeyAB darknet에 내장)한 가중치 파일을 사용할 수도 잇음
- obj.names
    annotation에 포함되어잇는 라벨링 이름 목록 -> 검출하고자 하는 목록
- images 
    학습 시킬 이미지 들
    .png or .jpg 등의 이미지로서 train image 및 val image 필요
    valid image는 train image의 10~20% 정도 설정
- annonation;
    학습 시킬 이미지에 대한 주석들
    주석 형식
        - [class-id] [center-x] [center-y] [w] [h]
    각 이미지마다 주석들이 담긴 텍스트 파일 필요
- train.txt
    학습 시킬 이미지들의 경로가 담긴 리스트
- valid.txt
    학습 시 validation 할 이미지들의 경로가 담긴 리스트
