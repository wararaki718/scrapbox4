from text import min_edit_distance


def main():
    source = "execution"
    target = "extention"

    distance = min_edit_distance(source, target)
    print(f"distance({source}, {target}): {distance}")
    print("DONE")


if __name__ == "__main__":
    main()
