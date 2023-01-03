import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

hotels = pd.read_csv('hotel_bookings.csv')

def create_catplot(x):
    sns.catplot(x=x, kind='count', data=hotels).set(title = 'Bar chart of {} column'.format(x))

def create_violinplot(df, column1, column2, column3):
    fig = sns.violinplot(data = df, x = column1, y = column2, hue = column3, inner="quartile", split=True, palette="prism") 
    sns.move_legend(fig, "upper left", bbox_to_anchor=(1, 1)) 
    plt.suptitle("Relationship between {0} and {1} columns".format(column1, column2), weight = 'demi', size = 'xx-large')    
