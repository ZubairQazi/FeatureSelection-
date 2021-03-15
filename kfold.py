import random
import numpy as np
import pandas as pd


def cross_validation(feature, current_features, idx):
    data = pd.read_csv('data/CS170_SMALLtestdata__70.txt', delim_whitespace = True, header = None)
    correctly_classified = 0

    # FIXME: iterate over number of rows
    for i in range(10):
        objects_to_classify = data.iloc[i, 1:]
        label = data.iloc[i, 0]

        nn_distance = nn_location = 1000000.0
        nn_label = 0.0

        # FIXME: iterate over number of rows
        for j in range(10):
            if i != j:
                # print('Ask if {} is nearest neighbors with {}'.format(i+1, j+1))
                distance = np.sqrt(sum(pow(objects_to_classify - data.iloc[j, 1:], 2)))
                if distance < nn_distance:
                    nn_distance = distance
                    nn_location = j
                    nn_label = data.iloc[nn_location, 0]

        if label == nn_label:
            correctly_classified += 1

        print('Object {} is in class {}'.format(i+1, label))
        print('Its nearest neighbor is {} which is in class {}'.format(nn_location, nn_label))

    # FIXME: Update 10 to number of rows
    accuracy = correctly_classified / 10
    return accuracy


if __name__ == '__main__':
    cross_validation([], [], 0)
