import pandas as pd
import matplotlib.pyplot as plt

class PlotPerDate:
    def __init__(self,df,state):
        self.state = state
        self.df = df

    def plot(self):
        state_df = self.df[self.df['state'] == self.state]
        state_df.set_index('date')['newCases'].plot(
            figsize=(10, 5),
            title=f'Casos diários em {self.state}'
        )
        plt.xlabel('Data')
        plt.ylabel('Novos Casos')
        plt.grid(True)
        plt.show()  