# 회고

깊이 우선 탐색 알고리즘인 DFS는 스택 자료구조에 기초한다. 즉, 재귀 함수로 구현할 수 있다.

DFS의 구체적인 동작 과정

1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

재귀 함수를 사용할 때는 재귀 함수가 언제 끝날지, 종료 조건을 꼭 명시해야 한다는 것을 기억하자.

그래프는 2가지 방식으로 표현할 수 있다.

- 인접 행렬: 2차원 배열로 그래프의 연결 관계를 표현, 모든 관계를 저장한다.

- 인접 리스트: 리스트로 그래프의 연결 관계를 표현, 연결된 정보만을 저장한다.