import threading

import treading
import time


def handler(started=0, finished=0):
    result = 0
    for i in range(started,finished):
        result += i
    return result


params = {'finished': 2 ** 26}

task = threading.Thread(target=handler, kwargs=params)
started_at = time.time()
print('res1')
task.start()
task.join()
print('{}'.format(time.time() - started_at))

started_at = time.time()
print('res2')
handler(**params)
print('{}'.format(time.time() - started_at))
