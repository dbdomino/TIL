defunct 

실행을 완료했지만 프로세스 테이블에서 Parent 프로세스에 완료 상태를 전달하지 못한 프로세스를 Defunct 프로세스라고 부른다.
Child 프로세스는 항상 프로세스 테이블에서 제거되기 전 먼저 Defunct 상태가 되고,
Parent 프로세스는 프로세스 테이블에서 Child 프로세스 항목을 가져와 Child 프로세스의 종료 상태를 읽는다..

Child 프로세스가 종료되면 대부분의 Parent 프로세스는 종료 코드를 얻기 위해 대기한다.
종료 코드는 프로세스 테이블에 저장되고, 종료 코드를 읽는 행위를 "Reaping"이라고 하는데,
Child 프로세스의 종료 코드를 Parent 프로세스에서 Reaping 하지 못하면, Child 프로세스는 Defuct 프로세스가 되는 것이다. 

결론적으로 Defunct 프로세스란 Child 프로세스는 이미 종료되었지만,
Parent 프로세스가 종료의 상태를 알 수 없을 경우 Child 프로세스는 Defuct 상태가 된다.

Defunct 프로세스는 프로세스 테이블에서 공간만 차지한다.
메모리나 CPU를 사용하지 않지만 프로세스 테이블은 RAM에 저장되는 유한한 리소스이고,
과도한 Defunct 프로세스를 만든다면 다른 프로세스에 영향을 줄 수 있기 때문에 항상 피해야한다.

[CreatePlan](./asset/zombie1.png)

defunct 기억하기
