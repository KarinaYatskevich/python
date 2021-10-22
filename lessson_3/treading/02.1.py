import threading

print(threading.active_count())
current = threading.current_thread()
print(current.getName())
print(current.is_alive())

try:
    current.start()
except RuntimeError as e:
    print('{error}'.format(error=e))
current.setName('sup')
print(current.getName())

print(threading.enumerate())

thread_data = threading.local()
thread_data.value = 5


def print_results():
    print(threading.current_thread())
    print('{}'.format(thread_data.value))


def counter(started, to_value):
    print(hasattr(thread_data, 'value'))
    thread_data.value = started
    for i in range(to_value):
        thread_data.value += 1
    print_results()


task1 = threading.Thread(target=counter, args=(0,10), name='Task1')
task2 = threading.Thread(target=counter, args=(100, 3), name='Task2')
task1.name = 'task1'
task2.name = 'task2'

task1.start()
task2.start()

print_results()


