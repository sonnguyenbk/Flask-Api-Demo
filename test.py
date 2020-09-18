class Test:

    a = 1

    def __init__(self, a):
        a = a


if __name__ == "__main__":
    a = Test(2)
    Test.a = 2

    print(Test.a)