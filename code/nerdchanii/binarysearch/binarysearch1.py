import time
'''
2021.09.01-2021.09.02
처음으로 Lv.3문제를 풀었다 ㅜ.ㅜ..
'''

def solution(n: int, times: list):   	
	# left = 가능한 최소시간
    left= 1 
	# right = 가능한 최장 시간
    right= max(times)*n
	# left ........ right

    while left<right:
		# 최소와 최장 시간 사이 시간 mid
        mid = (left+right)//2
		#mid 시간 동안 심사관들이 각각 볼 수 있는 사람 수를 리스트로 만듬
        how_many = [mid//t for t in times]
		# how_many의 합계가 n(검사해야하는 사람 수)보다 많거나 같으면, mid를 최장시간으로 다시 설정
        if sum(how_many)>=n:
            right= mid
        # how_mnay의 합계가 n보다 작으면, mid분(시간)보다 많이 필요하므로 최소시간을 mid+1분으로 설정
        else:			
            left= mid+1
		# left가 right를 넘어가면 탐색을 마침
    return left

if __name__ == '__main__':
	#testcase를 위한 값
    start =time.time()
	# testcase 1 
    n = 6
    times= [7,10]
	# testcase == result값과 일치하는지 확인
    if solution( n , times) == 28:
        print("success")
    end= time.time()
	# 실행시간을 출력
    print(f"{(end-start)*1000:.3f}s")