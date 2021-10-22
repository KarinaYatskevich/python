def main():
    c = {'name': 'karina'}
    try:
        print(c['url'])
    except:
        print('no')
    s = 1+1
    print(s)   




def main2():
    a = 'name'
    try:
        ac = a[5]
    except:
        print('no') 
    print(a.upper())


def main3():
    a = [1, 3, 7]
    b = a.pop(0)
    try:
        print(b)
    except:
        print('no') 
    print(a)

def main4(a):
    try:
        b = 10/a
    except ZeroDivisionError as err:         
        print(f'{err}')

main4(0)            

