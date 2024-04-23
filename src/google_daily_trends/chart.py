import matplotlib.pyplot as plt


class BarData:
    def __init__(self):
        pass

    def visualize_data(self, first_list, second_list):
        fig, ax = plt.subplots(figsize=(20, 10))
        fix_list = []
        print(first_list)
        print(second_list)
        for i in second_list:
            fix_list.append(int(i.split("+")[0]))
        print(fix_list)
        bar_labels = ['red', 'blue', '_red', 'orange']
        ax.bar(first_list, fix_list, label=first_list)
        ax.set_ylabel('search numbers')
        ax.set_xlabel('search numberssas')
        ax.set_title('Daily trends')
        ax.legend(title='Fruit color')
        plt.show()

# fig, ax = plt.subplots()
#
# fruits = ['apple', 'blueberry', 'cherry', 'orange']
# counts = [40, 100, 30, 55]
# bar_labels = ['red', 'blue', '_red', 'orange']
# bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
#
# ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
#
# ax.set_ylabel('fruit supply')
# ax.set_title('Fruit supply by kind and color')
# ax.legend(title='Fruit color')
#
# plt.show()
