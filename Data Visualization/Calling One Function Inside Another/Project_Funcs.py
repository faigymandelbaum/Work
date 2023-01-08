import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def create_boxplot(x, df):
    sns.boxplot(x=x, data=df).set(title = 'Box Plot of {} column'.format(x))


def func1(x, df):
    print (df[x].value_counts())
    print("The above reflects the range of values for {} column".format(x))
    create_boxplot(x, df)

def create_histplot(number, number2, df1, df2, df3, df4, title, title2):
    fig, axes = plt.subplots(2,2, figsize = (12,10))
    word="Cancelled "
    sns.histplot(ax = axes[number, number], data = df1, hue = 'hotel',x = 'lead_time', palette='prism', kde = True).set_title(word+title, weight = "demi")
    sns.histplot(ax = axes[number, number2], data = df2, hue = 'hotel',x = 'lead_time', palette='prism', kde = True).set_title(word +title2, weight = "demi")
    sns.histplot(ax = axes[number2, number], data = df3, hue = 'hotel',x = 'lead_time', palette='prism', kde = True).set_title(title, weight = "demi")
    sns.histplot(ax = axes[number2, number2], data = df4, hue = 'hotel',x = 'lead_time', palette='prism', kde = True).set_title(title2, weight = "demi")

def func2(number, number2, df1, df2, df3, df4, title, title2):
    print('Function 2')
    create_histplot(number, number2, df1, df2, df3, df4, title, title2)     
