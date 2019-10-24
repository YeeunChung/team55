# team55, Polaris 3D
- 2019 졸업 프로젝트 상반기팀
- 1615075 허유경, 1615052 이원선, 1615066 정예은
- 산학 프로젝트
- 지도 교수님: 민동보 교수님

---
### 1. show_depth.py
intel zr300 카메라를 사용하여 color image, depth image를 받아오고 저장하는 코드.
ubuntu 환경 기반 python으로 작성되었음.

### 2. fcrn_train.py
FCRN 논문을 기반으로 작성된 training code.

### 3. gen_tfrecord.py
training dataset과 validation dataset을 읽어와 tfrecord 형식으로 바꿔주는 코드.

### 4. predict_test.py
학습을 통해 만들어 낸 ckpt 파일을 통해 test하는 코드.

### 5. gen_predict.py
test(predict)를 위해 test dataset을 tfrecord 형식으로 바꿔주는 코드.

### 6. reverse/reverse.py
depth image를 색 반전 시켜주는 코드.
python opencv 사용.

### 7. shuffle.py
전체 dataset에 대하여 training dataset : validation dataset = 8 : 2로 random하게 나누어 저장해 주는코드.
python 사용.

### 8. makedata/checknull.py
특정 폴더에 비어 있는 파일이 있는지 확인하는 코드.
python 사용.

### 9. makedata/matchcd.py
c, d 폴더의 모든 파일명이 같은지 검사하는 코드.
python 사용.

### 10. makedata/btow.py
데이터 전처리 과정으로, 범위를 벗어난 검은 부분을 흰색으로통일시키는 코드.
python 사용.

### 11. makedata/opening.py
흰 hole 부분을 채우는 코드.
python 사용.

### 12. makedata/reverse.py
특정 폴더에 있는 이미지들을 색 반전시켜주는 코드.
python 사용.
 
---
* 2-5는 tensorflow ver 1.13.1, python ver 2.7.16 기반으로 작성되었음.
* https://github.com/Windaway/FCRN-Depth-Prediction-Tensorflow 을 참고하여 작성하였음.
