from multiprocessing import Queue

CustomQueue = Queue(maxsize=3)
CustomQueue.put(1)
CustomQueue.get(1)