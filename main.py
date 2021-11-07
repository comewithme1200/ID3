from chefboost import Chefboost as chef
import pandas as pd


df = pd.read_csv("tests/dataset/golf.csv")
config = {'algorithm': 'ID3'}
model = chef.fit(df, config=config, target_label='Decision')

