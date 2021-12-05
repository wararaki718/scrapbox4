from typing import List, Type

from sample import Sample


def get_methods(MyClass: Type[Sample]) -> List[str]:
    methods = dir(Sample)
    methods = list(filter(lambda x: not (x.startswith("__") or x.endswith("__")), methods))
    return methods


def main():
    sample = Sample()
    sample.sample1()
    sample.test1()

    print(dir(Sample))
    print()
    print(get_methods(Sample))
    print("DONE")

if __name__ == "__main__":
    main()
