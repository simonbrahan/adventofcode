import threading, time

class Worker:
    def __init__(self, time_to_work):
        self.time_to_work = time_to_work
        print 'worker', threading.currentThread().getName(), 'working for', time_to_work, 'seconds'

    def start(self, start_time):
        self.started = start_time

    def finished(self):
        return int(time.time()) > self.started + self.time_to_work


start = int(time.time())
workers = []
for i in range(10):
    worker = Worker(i)
    workers.append(worker)
    t = threading.Thread(
        name="thread " + str(i),
        target=worker.start,
        args = (start,)
    )
    t.start()


while True:
    if all(worker.finished() for worker in workers):
        print 'finished in', int(time.time()) - start, 'seconds'
        break
