# Functions in functions
import seaborn as sns
import matplotlib.pyplot as plt

def create_heatmap(df):    
    sns.heatmap(df.corr(), cmap = 'PiYG',linewidths=0.8)
    plt.suptitle('{} Values Correlations'.format(df), weight = 'bold', size = 'x-large')
    plt.show()
    print('''It seems that there is no strong correlation between columns,
     aside for a relationship between arrival date week number 
     and the arrival date year.
     We are continuing to investigate correlations individually.''')

def plotting_plots(df):
    create_heatmap(df)



