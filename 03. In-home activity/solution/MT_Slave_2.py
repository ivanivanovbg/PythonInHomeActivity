from multiprocessing import Queue
from time import sleep
def do_loop(queue1:Queue):
    i = 0
    maxi = 100000
    while not i == maxi:
        queue1.put("Proc 2 : " + str(i))
        sleep(0.1)
        i+=1