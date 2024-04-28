import datetime
import webbrowser
import randomcolor

import matplotlib.pyplot as plt



class BarData:
    def __init__(self):
        self.bar_to_url = ""

    def on_pick(self, event):
        bar = event.artist
        if bar in self.bar_to_url:
            webbrowser.open(self.bar_to_url[bar])

    def visualize_data(self, first_list, second_list, third_list):
        fig, ax = plt.subplots(num=f'Trends of {datetime.date.today().strftime("%d %B, %Y")}')  # "%d %B, %Y"
        fix_list = []
        colors = []
        for list_length in range(len(first_list)):
            color = randomcolor.RandomColor().generate()
            colors.append(color[0])
        for i in second_list:
            fix_list.append(int(i.split("+")[0]))
        bars = ax.bar(first_list, fix_list, label=first_list, color=colors, picker=5)
        self.bar_to_url = {bar: url for bar, url in zip(bars, third_list)}
        fig.canvas.mpl_connect('pick_event', self.on_pick)
        ax.set_ylabel('search numbers')
        ax.set_xlabel('trend names')
        ax.tick_params(axis='y', labelsize=8)
        ax.set_xticklabels([])
        ax.set_title('Daily trends')
        ax.legend(title='Trend Names')
        plt.show()
