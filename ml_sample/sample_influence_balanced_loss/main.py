from loader import get_cifer_loaders
from model import NNModel
from train import train, train_ibloss
from valid import valid, valid_each_class
from utils import try_gpu


def main():
    train_loader, test_loader, class_names = get_cifer_loaders(batch_size=32)

    print("cross-entropy")
    model = NNModel(len(class_names))
    model = try_gpu(model)

    print("start training:")
    model = train(model, train_loader, class_names)
    print("end training:")
    print()

    print("start test:")
    _ = valid(model, test_loader)
    print()

    _ = valid_each_class(model, test_loader, class_names)
    print()
    print("end test:")
    print()

    print("ibloss")
    model = NNModel(len(class_names))
    model = try_gpu(model)

    print("start training:")
    model = train_ibloss(model, train_loader, class_names)
    print("end training:")
    print()

    print("start test:")
    _ = valid(model, test_loader)
    print()

    _ = valid_each_class(model, test_loader, class_names)
    print()
    print("end test:")

    

    print("DONE")


if __name__ == "__main__":
    main()
