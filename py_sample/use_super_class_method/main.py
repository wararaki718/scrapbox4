from sample import Sample, SuperSample


def main():
    super_sample = SuperSample()
    sample = Sample()

    print(super_sample.get_name())
    print(sample.get_name())
    print("DONE")


if __name__ == "__main__":
    main()
