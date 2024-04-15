from threading import Thread
from time import sleep

def threaded_function(arg):
    for i in range(arg):
        print("running")
        sleep(1)

def threaded_function2(arg):
    for i in range(arg):
        print("I am also running")
        sleep(1)



if __name__ == "__main__":
    thread = Thread(target = threaded_function, args = (5, ))
    thread2 = Thread(target = threaded_function2, args = (5, ))
    thread.start()
    thread2.start()
    # thread.join()
    print("thread finished...exiting")