# 회고

퀵 정렬은 기준 데이터를 설정하고, 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법이다.

가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(Pivot)로 설정한다.

가장 많이 사용되는 정렬 알고리즘이다.

퀵 정렬은 평균 O(NlogN)의 시간 복잡도를 가지지만, 최악의 경우 O(N^2)의 시간 복잡도를 가진다.

최악의 시간 복잡도를 가지는 경우는 첫 번째 원소를 피벗으로 삼을 때, 이미 정렬된 배열에 대해 퀵 정렬을 수행할 때이다.