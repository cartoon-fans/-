"""
二级界面处理
"""
def fun():
    while True:
        print("""1.xxxx
    2.yyyy
    3.zzzz
        """)
        cmd = input(">>")
        if cmd == '1':
            pass
        elif cmd == '2':
            pass
        elif cmd == '3':
            break

while True:
    print("""1.aaa
2.bbb
3.ccc
    """)
    cmd = input(">>")
    if cmd == '1':
        fun()
    elif cmd == '2':
        fun()
    elif cmd == '3':
        break