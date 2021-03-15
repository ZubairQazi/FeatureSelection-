import random
import pandas as pd


def cross_validation(feature, current_features, idx):
    data = pd.read_csv('data/CS170_SMALLtestdata__70.txt', delim_whitespace = True, header = None)

    # FIXME: iterate over number of rows
    for i in range(10):
        objects_to_classify = data.iloc[i, 1:]
        label = data.iloc[i, 0]

        nn_distance = nn_location = -1

        # FIXME: iterate over number of rows
        for j in range(10):
            if i != j:
                print('Ask if {} is nearest neighbors with {}'.format(i+1, j+1))

        # print('Looping over i at location', i+1)
        # print('Object {} is in class {}'.format(i+1, label))

    return random.randint(1, 10)


if __name__ == '__main__':
    cross_validation([], [], 0)
