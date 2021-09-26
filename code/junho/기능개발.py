import math
def solution(progresses, speeds):
    answer = []
    complete_day=0;
    reserve=0;
    count=0;
    for i in range(len(progresses)):
        reserve=100-progresses[i]
        if(i==0): #첫번째 배포시 필요한 일수를 조건문으로 구하였습니다. 이렇게 하면 반복문으로 구해야했던 첫번쨰 배포일까지의 반복이 줄어들게 됩니다. 
            complete_day=math.ceil(reserve/speeds[i])
            count=count+1;
        elif(i!=0): #이후 첫번쨰 배포일보다 크거나 같으면 같이 배포하고 아닐 경우 두번쨰 배포일을 구해서 배포일정을 잡습니다. 
            if(complete_day>=math.ceil(reserve/speeds[i])):
                count=count+1;
            elif(complete_day<math.ceil(reserve/speeds[i])):
                answer.append(count)
                count=0;
                complete_day=math.ceil(reserve/speeds[i])
                count=count+1;
            if(i==(len(progresses)-1)): #마지막 배포시 결과값을 append하여 마지막 값이 배포일보다 클 경우에도 배포가 되도록 처리해줍니다. 
                print('last')
                answer.append(count)
        
    return answer