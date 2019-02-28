# /usr/bin/python3

__author__ = "Sanju Sci"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright © 2019"


import matplotlib.pyplot as plt


class Visualize(object):

    def __init__(self):
        pass

    def make_chart_line_chart(self):
        """
        Function make_chart_line_chart
        This function is used to make a simple line chart.
        :return:
        """
        years = [2010, 2020, 2030, 2040, 2050, 2060, 2070]
        gdp = [500.34, 634.54, 890.76, 2035.45, 5978.7, 10243.6, 15786.9]

        # create a line chart, years on x-axis, gdp on y-axis
        plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

        # add a title
        plt.title("GDP")

        # add a label to the y-axis
        plt.ylabel("Billions of Rupee")
        plt.show()

    def make_chart_bar_chart(self):
        """
        Function make_chart_bar_chart
        This function is used to make a simple bar chart.

        :return:
        """
        movies = ["Story", "French Cinema", "A Calls", "Bright", "Foxtrots"]
        num_oscars = [10, 2, 4, 9, 18]

        # bars are by default width 0.8, so we'll add 0.1 to the left coordinates
        # so that each bar is centered
        xs = [i + 0.1 for i, _ in enumerate(movies)]

        # plot bars with left x-coordinates [xs], heights [num_oscars]
        plt.bar(xs, num_oscars)
        plt.ylabel("# of Academy Awards")
        plt.title("My Favorite Movies")

        # label x-axis with movie names at bar centers
        plt.xticks([i + 0.1 for i, _ in enumerate(movies)], movies)

        plt.show()


if __name__ == "__main__":
    v = Visualize()
    v.make_chart_line_chart()
    v.make_chart_bar_chart()



