## Git 원격 저장소

---

깃 원격 저장소 기능을 제공해주는 서비스는 `gitlab`, `bitbucket`, `GitHub` 등이 있다



## 원격 저장소 설정

```bash
$ git remote add origin {url}
$ git remote add origin https://github.com/SOL-2/TIL.git
```

* Git, 원격저장소를 추가(`add`)하고 `origin` 이라는 이름으로 `url` 으로 설정

* 설정된 저장소를 확인하기 위해서는 아래의 명령어를 사용

  ```bash
  $ git remote -v
  
  origin	https://github.com/SOL-2/TIL.git (fetch)
  origin	https://github.com/SOL-2/TIL.git (push)
  ```



## 원격저장소에 `push`

```bash
$ git push origin master

git push -u origin master
Username for 'https://github.com':   SOL-2
Password for 'https://SOL-2@github.com': 
Enumerating objects: 10, done.
Counting objects: 100% (10/10), done.
Delta compression using up to 8 threads
Compressing objects: 100% (9/9), done.
Writing objects: 100% (10/10), 305.77 KiB | 12.74 MiB/s, done.
Total 10 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/SOL-2/TIL.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```







