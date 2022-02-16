import pandas as pd
import datetime
import numpy as np

def get_data(path="../data/temps.csv"):
    df = pd.read_csv("../data/temps.csv")
    # replace outliers with previous day
    df.iloc[287, 4] = df.iloc[286, 4]
    df.iloc[286, 5] = df.iloc[285, 5]
    # one hot encode weekdays
    df_enc = pd.get_dummies(df)
    # convert datetimes
    unix_days = []
    zero = datetime.date(year=1, month=1, day=1)
    for _, row in df_enc.iterrows():
        unix_days.append((datetime.date(year=int(row["year"]), month=int(row["month"]), day=int(row["day"])) - zero).days)
    df_enc["unix_days"] = unix_days
    df_enc = df_enc.drop(columns=["year", "day"])
    return df_enc
