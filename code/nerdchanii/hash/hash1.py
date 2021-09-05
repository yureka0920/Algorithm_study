'''
2021.09.04
백준 알고리즘 15829번 해슁
https://www.acmicpc.net/problem/15829

'''

# 입력받기
len_s = int(input())
get_alpa = input()

# sum을 저장하기 위함
s = 0
for i in range(0,len_s):
    # get_alpa로 입력받은 문자열의 각 자리를 아스키코드값으로 전환해서 96씩 뺌
    # 'a' = 97 임므로 'a'= 1이 됨 
    # 각 자리마다 31의 지수를 0부터 1씩 증가시키므로 (31**i)
    s += (ord(get_alpa[i])-96)*(31**i)

# 해쉬값을 구하는 것이므로 s% 1234567891로 나눠줌
print(s%1234567891)