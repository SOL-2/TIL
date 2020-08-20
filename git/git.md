## Git 기초

---

깃을 윈도우에서 활용하기 위해서는 [git bash]를 설치해야한다

> Git은 분산형 버전관리시스템(DVCS)이다.

## 1. 저장소 초기화

```bash
git init

Initialized empty Git repository in /Users/janghansol/TIL/.git/

(master)$
```

* 로컬 저장소를 만들고 나면, `.git/` 폴더가 생성되고 bashdp `master`라고 표표시시된다
* 반드시 저장소를 만들기전에 원하는 디렉토리인지 확인하는 습관을 가지고 저장소 내부에 저장소를 만들지 말자!! 
  * 경로확인 필수



## 2. add

작업한 내용을 커밋 대상 목록에 추가한다.

```bash
# 작업 후 상태 
On branch master

No commits yet
# git으로 관리된 적 없는 파일

Untracked files:
# 커밋 될 것들에 포함시키기위해서는 add 명령어를 써라
  (use "git add <file>..." to include in what will be committed)
	git.md
	markdown-images/
	markdown.md

# 커밋될 곳에 없다
# 하지만 새로 생성한 파일은 존재한다(untracked files)
nothing added to commit but untracked files present (use "git add" to track)

```

```bash
# add 명령어 후 상태

$ git status

On branch master

No commits yet
# 커밋이 될 변경사항들
# working directory x
# staging area o

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   git.md
	new file:   "markdown-images/\355\231\230\352\262\275\354\204\244\354\240\225 \354\202\254\354\247\204.png"
	new file:   markdown.md

```



## 3. commit

```bash
$ git commit -m 'add markdown'
[master (root-commit) 51cca18] add markdown
 3 files changed, 115 insertions(+)
 create mode 100644 git.md
 create mode 100644 "markdown-images/\355\231\230\352\262\275\354\204\244\354\240\225 \354\202\254\354\247\204.png"
 create mode 100644 markdown.md
```

* 커밋은 버젼을 기록하는 명령어
* 커밋 메시지는 해당하는 이력을 나타낼 수 있도록 작성하여야 함
* 커밋 이력을 확인하기 위해선 아래의 명령어를 사용한다



```bash
$ git log
commit 51cca1855b3efdbcb9e790fb71f70f6f4ae55e8e (HEAD -> master)
Author: Hansol Jang <kjhs0320@gmail.com>
Date:   Thu Aug 20 14:58:10 2020 +0900

    add markdown
    
$ git log -1
$ git log --oneline
$ git log --oneline -1
```



```bash

```

