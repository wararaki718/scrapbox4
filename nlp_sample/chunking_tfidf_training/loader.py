import pandas as pd


class DataLoader:
    def __init__(self, filepath: str, chunksize: int=50, batchsize: int=15):
        self._filepath = filepath
        self._chunksize = chunksize
        self._batchsize = batchsize
    
    def __iter__(self) -> pd.DataFrame:
        df = pd.read_csv(self._filepath, chunksize=self._chunksize)
        for chunk in df:
            for i in range(0, self._chunksize, self._batchsize):
                yield chunk.iloc[i:i+self._batchsize]
