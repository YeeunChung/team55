# team55, Polaris 3D
* 2019 졸업 프로젝트 상반기팀
* 1615075 허유경, 1615052 이원선, 1615066 정예은
* 산학 프로젝트
* 지도 교수님: 민동보 교수님
---
### 1. show_depth.py
intel zr300 카메라를 사용하여 color image, depth image를 받아오고 저장하는 코드.
ubuntu 환경 기반 python으로 작성되었음.

### 2. fcrn_train.py
FCRN 논문을 기반으로 작성된 training code.

### 3. gen_tfrecord.py
training dataset과 validation dataset을 읽어와 tfrecord 형식으로 바꿔주는 코드.

### 4. predict.py
학습을 통해 만들어 낸 ckpt 파일을 통해 test하는 코드.

### 5. gen_predict.py
test(predict)를 위해 test dataset을 tfrecord 형식으로 바꿔주는 코드.

---
* 2-5는 tensorflow ver 1.13.1, python ver 2.7.16 기반으로 작성되었음.
* https://github.com/Windaway/FCRN-Depth-Prediction-Tensorflow 을참고하여 작성하였음.
