from threading import Thread
from threading import current_thread

def thread_task(a, b, c, key1, key2):
    print("{0} received the arguments: {1}, {2}, {3}, {4}, {5}".format(current_thread().getName(),
                                                                       a, b, c, key1, key2))


myThread = Thread(
    group = None, #reserved for future extensions(optional)
    target = thread_task, #name of the piece of code to threaded, it can be an object of a function which has a __call__ function \
    name = "DemoThread",  #name the thread(optional)
    args = (1, 2, 3), #tuple is required to provide arguments
    kwargs = {"key1": 777,"key2": 334},  #dictionary is required to provide keyword arguments
    daemon = None
)



#starting the thread
myThread.start()

#wait for the thread to complete
myThread.join()