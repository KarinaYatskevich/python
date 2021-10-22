import threading
import time


def producer():
    time.sleep(10)
    print('Product found')
    product.set()
    product.clear()


def customer():
    print('wait')
    product.wait()
    print('exists')


product =threading.Event()

task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=customer)

task1.start()
task2.start()

task1.join()
task2.join()
