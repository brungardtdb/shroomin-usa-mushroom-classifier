import seaborn as sns
import matplotlib.pyplot as plt


# class for managing data visualizations
class DataVisualizer:

    def __init__(self, df):
        self.df = df

    # takes in a mushroom attribute and returns a count plot
    # that shows the occurrences of that attribute in the dataset
    def get_count_plot(self, field):
        fig = plt.figure(figsize=(10, 6), dpi=100)
        sns.countplot(data=self.df, x=field, hue="class")
        return fig

    # takes in a mushroom attribute and returns a heatmap
    # that shows the occurrences of that attribute in the dataset
    def get_heatmap(self, field):
        fig = plt.figure(figsize=(10, 6), dpi=100)
        ct = self.df[field].value_counts()
        ct = ct.to_frame()
        plt.subplots_adjust(bottom=0.35)
        sns.heatmap(data=ct, cmap='viridis')
        return fig

    # takes in a mushroom attribute and returns a pie chart
    # that shows the occurrences of that attribute in the dataset
    def get_pie_chart(self, field):
        fig = plt.figure(figsize=(10, 6), dpi=100)
        ct = self.df[field].value_counts()
        ct = ct.to_frame()
        palette_color = sns.color_palette('viridis')
        plt.pie(data=ct, x=field, labels=ct.index, colors=palette_color)
        return fig
