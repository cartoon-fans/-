# print("{1},{0},{1}".format("hello", "world"))
# print('{:o}'.format(11))
# s="      w e f #w e fs# d a g s a       "
# print(s.strip())
# print("--".join(s))
# print(s.split('#'))
def fun00(func):
    def waper(*args, **kwargs):
        print("修饰器的方法")
        return func(*args, **kwargs)

    return waper


@fun00
def fun01():
    print("这个是第一句话")


fun01()


def 函数装饰器名称(func):
    def wrapper(*args, **kwargs):
        print("装饰器语句")
        return func(*args, **kwargs)


    return wrapper


@函数装饰器名称
def 原函数名称():
    print("我有话想说")


原函数名称()
