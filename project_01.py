# -*- encoding:utf-8 -*-
import re
import requests
import random
from bs4 import BeautifulSoup


def demo_spider():
    content = requests.get('http://www.qiushibaike.com/').content
    soup = BeautifulSoup(content, 'html.parser')
    for div in soup.find_all('div', {'class': 'content'}):
        print div.text.strip()


def demo_set():
    seta = set((2, 3, 4))
    setb = set((1, 2, 3))
    print seta, setb
    seta.add(6)
    print seta.intersection(setb), seta & setb
    print seta | setb, seta.union(setb)
    print seta - setb
    seta.add('x')
    print seta
    print len(seta)


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def demo_dict():
    dicta = {4: 1, 1: 2, 3: 3, 5: 6}
    print dicta
    print 2, dicta.keys(), dicta.values()
    print 3, dicta.has_key(1), dicta.has_key('3')
    for val, key in dicta.items():
        print val, key
    # dicta['+'] = add
    # dicta['-'] = sub
    # print 'add: ',  dicta['+'](2, 3)
    dictb = {'+': add, '-': sub}
    print 'sub: ', dictb.get('-')(3, 2)
    print 'add: ', dictb['+'](4, 5)
    dictb['*'] = 'x'
    print dictb
    del dicta[1]
    print dicta


class User:
    type = 'USER'

    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def __repr__(self):
        return 'im' + self.name + ' ' + str(self.uid)


class Admin(User):
    type = 'ADMIN'

    def __init__(self, name, uid, group):
        User.__init__(self, name, uid)
        self.group = group

    def __repr__(self):
        return 'im' + self.name + ' ' + str(self.uid) + ' ' + self.group


def demo_exception():
    try:
        print 2 / 1
        print 2 / 0

        raise Exception('Raise Error', 'Nowcoder')
    except Exception as e:
        print 'error: ', e
    finally:
        print 'clean up'


def demo_random():
    random.seed(1)
    print 1, int(random.random() * 100)
    print 2, random.randint(0, 200)
    print 3, random.choice(range(0, 100, 10))
    print 4, random.sample(range(0, 100), 4)


def demo_re():
    str = 'abc123def12gh15'
    p1 = re.compile('[\d]+')
    p2 = re.compile('\d')
    print 1, p1.findall(str)
    print 2, p2.findall(str)

if __name__ == '__main__':
    # demo_dict()
    # demo_set()
    # user1 = User('u1', 1)
    # print user1
    # admin1 = Admin('a1', 101, 'g1')
    # print admin1
    # demo_exception()
    # demo_random()
    demo_re()
