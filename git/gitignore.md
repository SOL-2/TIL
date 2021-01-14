## gitignore

> 특정한 파일 및 폴더를 git으로 추적하지 않도록 설정

## .gitignore

---

* git 저장소 내부에 `.gitignore`파일을 생성한다
* git에서 제외시키고 싶은 형식을 지정한다

```bash
a.html     # a.html 특정 파일
secret/    # secret 특정 폴더
!secret/test.xlsx # secret 폴더 내의 test.xlsx는 gitignore에서 뺀다 => git으로 관리하겠다
*.xlsx     # 확장자가 .xlsx인 모든 파일
```



## 예시

* 일반적으로 특정 언어, 환경 변수, 특정 개발 환경(IDE, 텍스트에디터), 운영체제 관련된 파일들

[gitignore](gitignore.io) 접속하여 환경설정 선택하고 해당 문서를 작성한다.

해당 파일은 확장자 없음



Python -m venv venv

Source venv/scripts/activate



pip freeze > requirements.txt

Pip install -r requirements.txt

