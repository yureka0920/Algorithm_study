


def stack1(string: str):
    
    stack=0;
    print(len(string))
    for i in range(len(string)):
        if string[i]=='(':
            stack=stack+1
            print(stack,i)
        elif string[i]==')':
            stack=stack-1
            print(stack,i)
            if(stack<0):
                print('NO')
                break;
        if(i+1==len(string) and stack==0):
            print('YES')
        elif(i+1==len(string) and stack!=0):
            print('NO')

     
# stack1()          
# # def main():
# #     command_time =int(input())
# #     j = 0
# #     while(j < command_time):
# #     	input_list = list(input())
# #     	stack = list()
# #         if(stack1(stack,input_list) == 1):
# #     			print("yes")
# #         else:
# #             print("no")
# #         j+=1
# # if __name__ == '__main__':
# # 	main()