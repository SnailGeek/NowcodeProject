# -*- encoding=UTF-8 -*-

def log(level, *args, **kvargs):
    def inner(func):
        '''
        *代表无名字的参数
        ** 代表有名字的参数
        :param func:
        :return:
        '''

        def wrapper(*args, **kvargs):
            print level,"before called: ", func.__name__, '\n'
            print level,'ARGS:  ', args, 'kvargs: ', kvargs;
            func(*args, **kvargs)
            print level,"end called: ", func.__name__, '\n'
        return wrapper
    return inner



@log(level = 'INFO')
def hello(name, age):
    print 'hello world\n', name , age

@log(level='NOT')
def hello2(name):
    print 'hello', name




if __name__ == '__main__':
    hello2('TYJY')
    hello(name = 'tjy', age = 3)
