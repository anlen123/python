#import ctypes
#cc = ctypes.cdll.LoadLibrary("./sum.so")
#a = cc.jie(6)
#print(a)
import ctypes

ret = ctypes.cdll.LoadLibrary("./prime.so")

print(ret._is_prime(234))
