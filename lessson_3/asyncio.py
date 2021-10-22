import asyncio
import time
import requests
import os


async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(0.1)


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print(f"{count} seconds have passed")
        count += 1
        await asyncio.sleep(0.1)


async def print_twice():
    count = 0
    while True:
        if count % 2 == 0:
            print(f"{count} twice print!")
        count += 1
        await asyncio.sleep(0.1)


async def main():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())
    task3 = asyncio.create_task(print_twice())

    await asyncio.gather(task1, task2, task3)

LOREN_URL = 'https://loremflickr.com/320/240'
PATH_FOR_FILES = 'icons'


def get_file():
    responce = requests.get(LOREN_URL)
    if not responce:
        raise Exception('fail')
    return responce.url.split('/'[-1]), responce.content


def save_file(name, content):
    path_to_file = f'./{PATH_FOR_FILES}/{name}'

    with open(path_to_file, 'wb') as file:
        file.write(content)


if __name__ == '__main__':
    res = get_file()
    print(res)
    save_file(res[0], res[1])


# func > Future