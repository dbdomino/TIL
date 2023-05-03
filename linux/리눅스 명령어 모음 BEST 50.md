# 1. 파일 시스템 탐색을 위한 리눅스 명령어

* pwd 
  * pwd는 Print Work Directory의 약자이며, 현재 위치 경로를 보여줍니다.
* ls
  * list segments의 약자이며,  파일과 디렉터리의 모든 정보를 제공하며 특정 디렉터리와 특정 파일의 내용도 제공합니다. 
* cd
  * change directory의 약자이며, 경로변경에 사용됩니다.
* mkdir
  * 새로운 디렉토리를 만듭니다.
* rm, rmdir
  * rm은 파일을 삭제할 때 사용합니다.
  * rmdir은 remove directory의 약자, 빈 디렉터리를 삭제할 때 사용합니다.
* df
  * df 명령은 파일 시스템의 디스크 공간에 대한 정보를 표시하는 명령어 입니다.
  * df -h
* lsblk
  * Linux 시스템에서 사용 가능한 블록 장치를 나열해야 할 경우 사용됩니다.
  * df -h 와 기능이 비슷하여 같이 사용합니다.
* mount
  * 외부 디스크를 연결(cd, usb메모리, 외장하드 등) 할 때 mount를 자동으로 잡아주는 경우가 없는 리눅스에서
  * mount명령어로 외부 디스크를 특정 디렉토리와 연결해서 열어보고 사용하기 위한 명령어

# 2. 시스템 조작을 위한 리눅스 명령어

* shutdown
  * 시스템을 종료/재시작 할 때 사용함
* ps
  * 리눅스에서 동작하는 프로세스를 확인하는데 사용함
  * ps -ef
* kill
  * kill 명령어는 프로세스를 중지하고 없애는 역할을 한다.
  * kill -9 PID   https://server-talk.tistory.com/432
* 
