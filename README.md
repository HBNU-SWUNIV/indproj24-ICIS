# 한밭대학교 SW중심대학 산학연계프로젝트 <br/>- 사용자 수요 대응 JWT 운영 알고리즘 개발

## **팀 구성**
### 지도교수
 - 김태훈 교수님

### 기업체 
 - 오정민 대표

### 참여학생
 - 20201738 서민재
 - 20201761 김영권

## Project Background
- ### 필요성
  - 토큰의 유효시간이 줄어들면, 공격자가 토큰을 탈취하여 악용할 가능성이 줄어들어 보안적으로 안전해진다.<br/>
그러나 이로 인해 더 많은 토큰 요청이 발생해 서버에 부하가 커지는 문제가 발생하게 된다.<br/>
반대로, 토큰 유효시간을 늘리면 서버의 부담은 줄어들지만, 토큰 탈취 및 악용 가능성이 증가한다.<br/>
따라서, 토큰 유효시간을 최적화하여 JWT 방식의 보안성과 서버 부담 간의 균형을 맞추는 것이 본 과제의 필요성이다.<br/>
- ### 기존 해결책의 문제점
  - 세션 방식의 한계:
    - 세션은 서버 측 메모리에 SessionId를 저장하기 때문에 사용자가 많아질수록 메모리 부담이 커진다.
    - 서버 장애 발생 시 기존 세션이 모두 유효하지 않게 되어 사용자가 재로그인해야 하는 문제가 있다.<br/>
  - JWT 방식의 단점:
    - 토큰 유효시간이 길면 보안 문제가 발생할 가능성이 증가한다.
    - 유효시간이 짧으면 토큰 발급 요청이 많아져 서버 부하가 증가한다.<br/>

## System Design
  - ### System Requirements
    - JWT 인증로직:
      - Django Rest Framework 기반으로 회원가입 및 로그인 API 개발.
      - JWT 발급 및 검증 프로세스 설계.
    - 메트릭 수집 및 모니터링:
      - Prometheus를 사용하여 서버 성능 데이터를 수집.
      - CPU, 메모리, 네트워크 트래픽 데이터를 실시간으로 시각화.
    
## Case Study
  - ### Description
  
  
## Conclusion
  - ### 토큰 유효시간이 5분일 때, 보안성과 서버 부하 간 균형이 가장 적합한 것으로 나타났다.<br/>짧은 유효시간 설정은 보안을 강화하지만, 특정 시점에서 서버의 과부하를 초래할 수 있다.
  
## Project Outcome
