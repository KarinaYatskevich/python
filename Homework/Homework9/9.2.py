
print((lambda **kwargs: {k*2: v for k, v in kwargs.items()})(test = 5, europe = 3))
