import datetime
import randomcolor
import webbrowser

import matplotlib.pyplot as plt
import matplotlib.ticker as mat_ticker


class BarData:
    def __init__(self):
        self.bar_to_url = ""
        self.fix_list = []
        self.colors = []
        self.fig, self.ax = plt.subplots(num=f'Trends of {datetime.date.today().strftime("%d %B, %Y")}')

    def on_pick(self, event):
        bar = event.artist
        if bar in self.bar_to_url:
            webbrowser.open(self.bar_to_url[bar])

    def data_lists(self, first_list, second_list):
        for list_length in range(len(first_list)):
            color = randomcolor.RandomColor().generate()
            self.colors.append(color[0])
        for i in second_list:
            print(i)
            self.fix_list.append(int(i.split("+")[0]))
            print(self.fix_list)

    def set_the_parameters(self):
        self.ax.set_ylabel('search numbers')
        self.ax.set_xlabel('trend names')
        self.ax.tick_params(axis='y', labelsize=8)
        self.ax.set_xticklabels([])
        self.ax.set_title('Daily trends')
        self.ax.legend(title='Trend Names')
        self.ax.yaxis.set_major_formatter(mat_ticker.StrMethodFormatter('{x:,.0f}'))
        plt.show()

    def visualize_data_with_urls(self, first_list, second_list, third_list):
        self.data_lists(first_list, second_list)
        bars = self.ax.bar(first_list, self.fix_list, label=first_list, color=self.colors, picker=5)
        self.bar_to_url = {bar: url for bar, url in zip(bars, third_list)}
        self.fig.canvas.mpl_connect('pick_event', self.on_pick)
        self.set_the_parameters()

    def visualize_data_without_urls(self, first_list, second_list):
        self.data_lists(first_list, second_list)
        self.ax.bar(first_list, self.fix_list, label=first_list, color=self.colors)
        self.set_the_parameters()
