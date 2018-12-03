import time,multiprocessing

def square(listz):
    for i in listz:
        print("Current number is: ",i*i)
        time.sleep(3)

def cube(listz):
    for i in listz:
        print("Current number is: ",i*i*i)
        time.sleep(3)


if __name__=="__main__":
    lista=[1,2,3,4,5,6,7]
    t=time.time()

    process1=multiprocessing.Process(target=square,args=(lista,))
    process2=multiprocessing.Process(target=cube,args=(lista,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("time taken by the proram is",time.time()-t)
