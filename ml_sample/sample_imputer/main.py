import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.impute import SimpleImputer


def impute(imputer: SimpleImputer, data: pd.DataFrame) -> list:
    imputer.fit(data.age.values.reshape(-1, 1))
    
    filled_age = imputer.transform(data.age.values.reshape(-1, 1))
    print(f"[before] number of null: {data.age.isnull().sum()}")
    print(f"[after]  number of null: {(pd.Series(filled_age.flatten())).isnull().sum()}")
    return imputer.statistics_

def impute_multi(imputer: SimpleImputer, data: pd.DataFrame) -> list:
    imputer.fit(data[["age", "deck"]].values)
    
    filled_values = imputer.transform(data[["age", "deck"]].values)
    print(f"[before] number of null: {data[['age', 'deck']].isnull().sum()}")
    print(f"[after]  number of null: {pd.DataFrame(filled_values).isnull().sum()}")
    return imputer.statistics_


def main():
    data = sns.load_dataset("titanic")
    print(data.shape)

    data["deck"] = pd.Categorical(data.deck)
    data["deck"] = data.deck.cat.codes.apply(lambda x: x if x != -1 else np.nan)
    
    print("mean imputer:")
    mean_imputer = SimpleImputer(strategy="mean", missing_values=np.nan)
    statistics = impute_multi(mean_imputer, data)
    print(f"statistics: {statistics}")
    print()

    print("median imputer:")
    median_imputer = SimpleImputer(strategy="median", missing_values=np.nan)
    statistics = impute(median_imputer, data)
    print(f"statistics: {statistics}")
    print()

    print("most_frequent imputer:")
    frequent_imputer = SimpleImputer(strategy="most_frequent", missing_values=np.nan)
    statistics = impute(frequent_imputer, data)
    print(f"statistics: {statistics}")
    print()

    print("constant imputer:")
    constant_imputer = SimpleImputer(strategy="constant", missing_values=np.nan, fill_value=123)
    statistics = impute(constant_imputer, data)
    print(f"statistics: {statistics}")
    print()
    
    print("DONE")


if __name__ == "__main__":
    main()
