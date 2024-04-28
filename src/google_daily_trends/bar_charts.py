import datetime

import matplotlib.pyplot as plt
import randomcolor


class BarData:
    def __init__(self):
        pass

    @staticmethod
    def visualize_data(first_list, second_list):
        fig, ax = plt.subplots(num=f'Trends of {datetime.date.today().strftime("%d %B, %Y")}')  # "%d %B, %Y"
        fix_list = []
        colors = []
        for list_length in range(len(first_list)):
            color = randomcolor.RandomColor().generate()
            colors.append(color[0])
        for i in second_list:
            fix_list.append(int(i.split("+")[0]))
        ax.bar(first_list, fix_list, label=first_list, color=colors)
        ax.set_ylabel('search numbers')
        ax.set_xlabel('trend names')
        ax.tick_params(axis='y', labelsize=8)
        ax.tick_params(axis='x', labelsize=6)
        ax.set_title('Daily trends')
        ax.legend(title='Trend Names')
        plt.show()
