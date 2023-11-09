class parent():
    a=10
    def __init__(self):
        self.b=100


class child(parent):
    def show(self):
        print(super().a)
        # print(super().b)


ob=child()
ob.show()           #10