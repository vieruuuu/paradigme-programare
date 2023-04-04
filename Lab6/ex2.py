class A:
    def __init__(self):
        print("Clasa A a fost rulata")


class B(A):
    def __init__(self):
        A.__init__(self)
        print("Clasa B a fost rulata")


class C(A):
    def __init__(self):
        A.__init__(self)
        print("Clasa C a fost rulata")


class D_old(B, C):
    def __init__(self):
        super().__init__()
        print("Clasa D a fost rulata")


class D_new(B, C):
    def __init__(self):
        C.__init__(self)
        print("Clasa D a fost rulata")


if __name__ == "__main__":
    x1 = D_old()

    print()
    print()

    x2 = D_new()
