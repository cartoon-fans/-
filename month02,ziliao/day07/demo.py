class Process:
    def start(self):
        # if ,while for....
        self.run()

    def run(self):
        pass

class A(Process):
    def run(self):
        print("hello world")

a = A()
a.start()