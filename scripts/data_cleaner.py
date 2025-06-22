import pandas as pd

class DataCleaner:
    def __init__(self, df):
        self.df = df

    def clean(self):
        self.df['date'] = pd.to_datetime(self.df['date'])
        self.df = self.df[['date', 'state', 'newCases', 'newDeaths']]
        self.df = self.df.dropna()
        return self.df