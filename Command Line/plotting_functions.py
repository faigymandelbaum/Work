import matplotlib.pyplot as plt
import seaborn as sns

# plots
def create_heatmap(df, plot_name, cmap = 'PiYG'):
    sns.heatmap(df.corr(), cmap = cmap, linewidths = 0.8)
    plt.suptitle('{} Dataset Correlations'.format(plot_name), weight = 'bold', size = 'x-large')
    plt.savefig('{} heatmap.png'.format(plot_name), bbox_inches='tight')
    plt.clf()

def create_histogram(df, column):
    sns.catplot(data = df, x = column, kind = 'count').set(title = 'Bar chart of {} column'.format(column)) 
    plt.savefig('{} histogram.png'.format(column), bbox_inches='tight') 
    plt.clf()

def create_boxenplot(df, column):
    sns.boxenplot(x = df[column]).set(title = 'Boxenplot of {} column'.format(column)) 
    plt.savefig('{} boxenplot.png'.format(column), bbox_inches='tight')
    plt.clf()

def create_boxplot(df, column):
    sns.boxplot(x = df[column]).set(title = 'Boxplot of {} column'.format(column)) 
    plt.savefig('{} boxplot.png'.format(column), bbox_inches='tight')
    plt.clf()

def create_violinplot(df, column1, column2, column3):
    fig = sns.violinplot(data = df, x = column1, y = column2, hue = column3, inner="quartile", split=True, palette="prism") 
    sns.move_legend(fig, "upper left", bbox_to_anchor=(1, 1)) 
    plt.suptitle("Relationship between {0} and {1} columns".format(column1, column2), weight = 'demi', size = 'xx-large') 
    plt.savefig('{} and {} columns violinplot.png'.format(column1, column2), bbox_inches='tight')
    plt.clf()

def create_scatter(df, column1, column2):
    sns.catplot(data = df, x = column1, y = column2, palette='prism').set(title = 'Scatter plot of the {0} and {1} columns'.format(column1, column2)) 
    plt.savefig('{} and {} columns scatterplot.png'.format(column1, column2), bbox_inches='tight')
    plt.clf()

def create_lineplot(df, column1, column2, column3 = None):
    sns.lineplot(data = df, x = column1, y = column2, hue = column3).set(title = 'Scatter plot of the {0} and {1} columns'.format(column1, column2))  
    plt.xticks(rotation = 45)
    if column3 == None:
       plt.savefig('{} lineplot.png'.format(column1), bbox_inches='tight')
       plt.clf()
    else:
       plt.savefig('{0} and {1} columns lineplot.png'.format(column1, column2), bbox_inches='tight')
       plt.clf()   

def create_displot(df, column1, column2, column3):
    sns.displot(data = df, x = column1, hue = column2, col = column3, palette='prism', kde = True)
    plt.suptitle('Histogram of {} column'.format(column1), weight = 'bold', size = 'x-large', y = 1.05)      
    plt.savefig('{} displot.png'.format(column1), bbox_inches='tight')
    plt.clf()

def split_data(df, column1, column2, column3, num):
    df_less = df[df[column1] < num]
    df_more = df[df[column1] > num]
    df_less_true = df[df[column2] == True]
    df_less_false = df[df[column2] == False]
    df_more_true = df[df[column2] == True]
    df_more_false = df[df[column2] == False]
    fig, axes = plt.subplots(2,2, figsize = (14,10))
    sns.histplot(ax = axes[0,0], data = df_less_true, hue = column3 ,x = column1, palette='prism', kde = True).set_title('Chart for {} column where = True'.format(column2), weight  = 'demi')
    sns.histplot(ax = axes[0,1], data = df_more_true, hue = column3 ,x = column1, palette='prism', kde = True).set_title('Chart for {} column where = False'.format(column2), weight  = 'demi')
    sns.histplot(ax = axes[1,0], data = df_less_false, hue = column3 ,x = column1, palette='prism', kde = True).set_title('Chart for {} column where = True'.format(column2), weight  = 'demi')
    sns.histplot(ax = axes[1,1], data = df_more_false, hue = column3 ,x = column1, palette='prism', kde = True).set_title('Chart for {} column where = False'.format(column2), weight  = 'demi')
    plt.suptitle('Hotel Bookings', weight = 'bold', size = 'xx-large', y = 1)
    plt.savefig('{} and {} columns subplots.png'.format(column1, column2), bbox_inches='tight')
    plt.clf()


