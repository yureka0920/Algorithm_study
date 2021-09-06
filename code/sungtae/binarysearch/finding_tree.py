# n = int(input())
# m = list(map(int, input().split()))
n, m = tuple(map(int, input().split())) # 나무의 개수와 필요한 길이 입력받아 변수로 저장
trees = list(map(int, input().split())) # 나무들의 길이 저장
def cutting(n, m, trees):
    h = 0 # 높이 변수를 조건문에 넣기 위해 변수 설정
    for i in trees:
        if i > h: h = i # 가장 높은 나무의 높이 찾아 h에 저장
    while True:
        h += -1 # 높이를 서서히 줄여나가며 최소한의 길이 찾기 위해 설정
        height = 0 # 자른 나무의 길이
        cutted_trees = [] # 자른 나무의 길이를 더하기 위해 리스트 작성
        for k in trees:
            if k > h:
                height = k - h
                cutted_trees.append(height)
                if sum(tuple(cutted_trees)) == m: return h

print(cutting(n, m, trees))
