import matplotlib.pyplot as plt
from search import print_menu


def graph_small():
    file_name = input('Enter a file name to use for the graph image: ')

    x = ['{5}', '{8, 5}', '{8, 10, 5}', '{8, ..., 4}', '{8, ..., 1}', '{8, ..., 6}', '{8, ..., 9}', '{8, ..., 7}',
         '{8, ..., 2}', '{All Features}']
    y = [0.827, 0.94, 0.937, 0.91, 0.877, 0.847, 0.82, 0.797, 0.767, 0.75]

    plt.figure(figsize=(20, 8))
    plt.bar(x, y)
    plt.xlabel = 'Current Feature Set'
    plt.ylabel = 'Accuracy'
    plt.savefig('graphs/{}.png'.format(file_name))


def graph_large():
    file_name = input('Enter a file name to use for the graph image: ')

    x = ['{14}', '{14, 20}', '{14, 20, 19}', '{14, ..., 46}', '{Omitted', 'For', 'Space}',
         '{14, ..., 12}', '{All Features}']
    y = [0.802, 0.978, 0.95, 0.91, 0, 0, 0, 0.612, 0.574]

    plt.figure(figsize=(20, 8))
    plt.bar(x, y)
    plt.xlabel = 'Current Feature Set'
    plt.ylabel = 'Accuracy'
    plt.savefig('graphs/{}.png'.format(file_name))


def graph_feature_selection():
    file_name = input('Enter a file name to use for the graph image: ')

    features, accuracies = print_menu()
    x = [str(val) for val in features.values()]
    y = [float(key) for key in features.keys()]

    plt.figure(figsize=(20, 8))
    plt.bar(x, y)
    plt.xlabel = 'Current Feature Set'
    plt.ylabel = 'Accuracy'
    plt.savefig('graphs/{}.png'.format(file_name))


if __name__ == '__main__':
    graph_feature_selection()
