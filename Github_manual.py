'''
# git 사용법
    1) github 가입

    2) git 설치 및 환경 설정
- git 다운 후 Git Bash 열기
>>
git config --global user.name "내 이름 입력"
git config --global user.email "내 이메일 입력"
git config --list
=> 중간에 이름하고 이메일 설정한 것 잘 들어갔는지 확인

    3) git 사용법
코딩 프로그램 중 Terminal에서 입력하기(pycharm)
>>
git init
: 맨 처음 프로젝트를 업로드할 때 입력해야 함
>>
git add .
: 전부 업로드하기(add 다음에 한 칸 띄우고 . 누름에 유의)
cf) git 파일명
: 특정 파일을 업로드하기
>>
git status
: git 상태 확인
>>
git commit -m "first commit"
: 히스토리 생성 cf) 2번째는 first commit -> second commit (일종의 버전)

    4) 히스토리 깃허브에 보내기
>>
git remote add origin https://github.com/이름명/git저장소명
: 깃허브 연결고리 추가(https://github.com/이름명/git저장소명는 깃허브 링크 복사 후 붙여넣기)
>>
git remote -v
: 연결고리 확인
>>
git push origin master
: master branch로 코드 전송
* github 사이트서 새로고침

    5) 코드 업데이트
>>
git add .
(cf) git init은 필요없음. 맨 처음 추가할때만 입력
전부 업로드하기
>>
git commit -m "first commit"
버전 바꾸기
>>
git push origin master
: master branch로 코드 전송
* github 사이트서 새로고침


# git 협업하는 경우
    1) 공유된 코드 사용하는 방법
- 깃허브 사이트 가서 [Code] 누른 후 링크 복사
- [Terminal] 가서 입력
>>
git clone + 복사한 링크 붙여넣기 + 폴더이름
>>
cd 폴더이름
code .

    2) 업데이트 코드 업로드
- [Terminal] 가서 입력
>>
git add.
git commit -m "ooo first commit"
git checkout -b 폴더이름
: 나만의 폴더(작업 공간)을 따로 만드는 것(임시)
cf) git push master는 최종버전에 올리는 것
=> 따라서 협업할 때는 함부로 업로드 하지 말 것!!!
git push origin 폴더이름
- 깃허브 사이트 가서 [Compare & pull request] 클릭
- 커멘트 입력 후 [Create pull request] 클릭 => master에 갈 수 있게 허락해주세요라는 의미
- MASTER 입장에서 합칠거면 [Merge pull request] 클릭
=> [Merge pull request] 클릭하면 Master에 합쳐지게 되는 것

    3) 업데이트된 코드 동기화시키기
>>
git pull origin master
'''