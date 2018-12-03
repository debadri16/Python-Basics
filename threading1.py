import time
import threading
def sqr(lst):
    for i in lst:
        print(i*i)
        time.sleep(.5)

def cub(lst):
    for i in lst:
        print(i**3)
        time.sleep(.5)

lst=[1,2,3,4,5,6,7]
t=time.time()
th1=threading.Thread(target=sqr,args=(lst,))
th2=threading.Thread(target=cub,args=(lst,))

th1.start()
th2.start()

th1.join()
th2.join()
print('time=',time.time()-t)