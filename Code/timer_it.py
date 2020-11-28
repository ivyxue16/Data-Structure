from timeit import Timer
import timeit
def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

t1 = Timer("test1()","from __main__ import test1")
print("concat %f second\n" %t1.timeit(number=1000))

t2 = Timer("test2()","from __main__ import test2")
print("append %f second\n" %t2.timeit(number=1000))

t3 = Timer("test3()","from __main__ import test3")
print("comprehension %f second\n" %t3.timeit(number=1000))

t4 = Timer("test4()","from __main__ import test4")
print("list range %f second\n" %t4.timeit(number=1000))

x = list(range(2000000))
popzero = timeit.Timer("x.pop(0)","from __main__ import x")
popend = timeit.Timer("x.pop()","from __main__ import x")
print(popzero.timeit(number=1000))
print(popend.timeit(number=1000))