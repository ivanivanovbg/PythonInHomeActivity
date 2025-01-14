from multiprocessing import Process,Queue
import MT_Slave as ms
import MT_Slave_2 as ms2
if __name__ == "__main__":
    queue1 = Queue()
    queue2 = Queue()
    p1 = Process(target=ms.do_loop,args=(queue1,))
    p1.daemon = True
    p1.start()
    p2 = Process(target=ms2.do_loop,args=(queue2,))
    p2.daemon = True
    p2.start()

    while True:
        if not queue1.empty():
            msg = queue1.get(False)
            print(msg)
        if not queue2.empty():
            msg2 = queue2.get(False)
            print(msg2)