import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from loguru import logger
from pathlib import Path


class DataHandler:
    def __init__(self, csv_path: str | Path) -> None:
        self.df = pd.read_csv(csv_path)

    def get_pct_missing(self) -> pd.DataFrame:
        pct_missing = pd.DataFrame(self.df.isnull().sum() / len(self.df), columns=["pct_missing"])
        pct_missing = pct_missing.sort_values(by="pct_missing", ascending=False)
        return pct_missing

    def drop_columns(self, columns: list) -> pd.DataFrame:
        self.df = self.df.drop(columns=columns)
        return self.df.head()

    def one_hot_encode(self, features: list, concat: bool = False) -> pd.DataFrame:
        ohe = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
        ohe_array = ohe.fit_transform(self.df[features])
        ohe_df = pd.DataFrame(ohe_array, columns=ohe.get_feature_names_out(features))
        logger.info(f"Number of new features: {ohe_df.shape[1]}")

        if concat:
            self.df = pd.concat([self.df, ohe_df], axis=1)
            return self.df.head()
        else:
            return ohe_df
