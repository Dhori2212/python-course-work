class parent_A:
    def displayA(self):
        print("This is the child class-A")


class child_B:
    def displayB(self):
        print("This is the child class-B from (B=>A)")


class child_C:
    def displayC(self):
        print("This is the child class-C from (C=>A)")

class child_D:
    def displayD(self):
        print("This is the child class-D from (=>B=>A)")

class child_E:
    def displayE(self):
        print("This is the child class-E from (E=>D=>B=>A),(E=.C=.A)")

