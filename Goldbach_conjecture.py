'''验证哥德巴赫猜想在4，N上成立'''
# 任一大于2的偶数都可写成两个素数之和
import numpy as np
import time
import  copy

N = (pow(10,7))

def prime(n):
    '''n为一个整数'''
    n = int(n)
    if (n<100):
        if(n in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]):
            return 1
        else:return 0
    else:
        list = np.arange(2, 1 + int(np.sqrt(n)))
        # list = np.arange(2, n)
        list = n % list
        if(np.any(list==0)):
            return 0
        else:return 1

if __name__=="__main__":
    # 得到2，N上的所有素数
    t1=time.time()
    prime_list = []
    for i in range(2,N):
        if(prime(i)==1):
            prime_list.append(i)
            print(i)
        else:pass
    prime_list = np.array(prime_list,dtype=np.int)
    result=np.array([4],dtype=np.int)
    add_vec = copy.deepcopy(prime_list)
    for i in range(len(prime_list)):
        process_vec = add_vec+prime_list[i]
        result=np.hstack((result,process_vec[(process_vec % 2)==0]))
        result = np.delete(result, (result > N))
        result = np.unique(result)
    result = np.delete(result, (result > N))
    t2= time.time()
    check=2*np.array(np.arange(2,1+int(N//2)),dtype=np.int)
    if(len(result)!=len(check)):
        print('长度不对应','哥德巴赫猜想在4，',N,'上不成立')
    else:
        error=result-check
        if(np.any(error!=0)):
            print('数据不对应','哥德巴赫猜想在4，', N, '上不成立')
        else:
            print('哥德巴赫猜想在4，', N, '上成立')
    print('用时',t2-t1,'秒')
