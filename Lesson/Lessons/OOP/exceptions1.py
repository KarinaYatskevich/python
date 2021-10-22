# создание своих ошибок
# 13.04
id = 0

class My(Exception):
    def __init__(self, id, message):
        super(My, self).__init__(f'inv book {id}: {message}')
        self.book_id = id

class Page(My):
    def __init__(self, id):
        super(Page, self).__init__(id, 'page inv')

class Age(My):
    def __init__(self, id):
        super().__init__(id, 'age inv')



class Book:
    def __init__(self, page, year, author,price):
        global id
        self.id = id

        if page > 500:
            raise Page(id)
        self.page = page

        if year < 2000 or year > 2020:
            raise Age(id)
        self.year = year

        self.author = author
        self.price = price
        id += 1




if __name__ == '__main__':

    try:
        Book(400, 1999, "noname", 400)
    except My as err:
        print(f'Err {err}')

    # a =5
    # b =0
    # try:
    #
    #      x =a / b
    #      print(x)
    # except Exception as err:
    #     print(f'Err {err}')







