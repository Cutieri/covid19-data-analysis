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

class PlotTotalPerState:
    def __init__(self,df):
        self.df = df

    def plotTotal(self):
        total_per_state = self.df.groupby('state')['newCases'].sum().sort_values(ascending=False)
        total_per_state.plot(
            kind = 'bar',
            figsize=(10, 5),
            title=f'Total cases per state',
            color = 'red'
        )
        plt.xlabel('State')
        plt.ylabel('Cases')
        plt.grid(axis= 'y')
        plt.show()  

class DeathsPerDay:
    def __init__(self, df, state):
        self.df = df
        self.state = state

    def deaths(self):
        state_df = self.df[self.df['state'] == self.state]

        state_df['date'] = pd.to_datetime(state_df['date'])
        state_df = state_df.sort_values('date')

        plt.figure(figsize=(12, 5))
        plt.plot(state_df['date'], state_df['newDeaths'], color='crimson')
        plt.title(f'Mortes diárias por COVID-19 - {self.state}')
        plt.xlabel('Data')
        plt.ylabel('Novas Mortes')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
