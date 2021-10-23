from config import Config
from loader import Loader
from preprocess import preprocessing
from ranknet import RankNet
from utils import try_gpu
from train import train
from valid import valid


def main():
    config = Config.load("config.yml")
    loader = Loader()
    train_df = loader.load(config.train_filename)
    valid_df = loader.load(config.valid_filename)

    X_train, y_train, train_df = preprocessing(train_df)
    X_valid, y_valid, valid_df = preprocessing(valid_df)

    model = try_gpu(RankNet(X_train.shape[1]))

    for epoch in range(1, config.n_epochs+1):
        print(f"## epoch {epoch:02d}:")
        model = train(model, X_train, y_train, config.batch_size, config.n_sampling_combs)
        valid(model, X_valid, y_valid, valid_df)
        print("")
    
    print("DONE")


if __name__ == "__main__":
    main()
