import inspect


class Base:
    def instance_method(self):
        print("instancemethod")

    @staticmethod
    def static_method():
        print("staticmethod")


class Base2(Base):
    def instance_method(self):
        super().instance_method()
        print("instancemethod2")
    
    @staticmethod
    def static_method():
        #super().static_method() // error
        print("staticmethod2")


def main():
    #Base.instance_method() // error
    Base.static_method()
    base = Base()
    base.instance_method()
    base.static_method()

    #Base2.instance_method() // error
    Base2.static_method()
    base2 = Base2()
    base2.instance_method()
    base2.static_method()
    print()

    for name in inspect.getmembers(base, inspect.ismethod):
        print(name)
    print()

    print("DONE")


if __name__ == "__main__":
    main()
