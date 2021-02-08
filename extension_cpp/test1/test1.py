import ctypes
from time import time
cpp = ctypes.CDLL('./cm.so')
 
def cm(n):
	res = 0
	for i in range(n+1):
		res += i
		res -= i
	return res
 
if __name__ == '__main__':
    num = 10000000
    s1 = time()
    print("cpp result = %d" % cpp.cm(num))
    print('cpp time consuming: ', time()-s1)
 
    s2 = time()
    print('python result:%d' % cm(num))
    print('python time consuming: ', time()-s2)