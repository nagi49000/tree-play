import pandas as pd
import datetime
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.utils import shuffle


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


def get_cross_val_scores(clf, X, y, cv):
    X_shuffle, y_shuffle = shuffle(X, y)
    scores = cross_val_score(clf, X_shuffle, y_shuffle, cv=cv, scoring="neg_mean_absolute_error")
    return scores
