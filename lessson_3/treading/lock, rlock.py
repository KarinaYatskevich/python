import threading

def producer():
    print('locking')
    with lock:
        print('done')
        with lock:
            print('great')
    print('release')


lock = threading.Lock()

task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=producer)

task1.start()
task2.start()

task1.join()
task2.join()
