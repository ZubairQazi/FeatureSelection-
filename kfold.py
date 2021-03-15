import random
import numpy as np
import pandas as pd


def cross_validation(complete_data, current_features, feature_to_add):

    # remove columns we are not interested in
    data = complete_data[[0] + list(current_features) + [feature_to_add]]
    correctly_classified = 0
    num_rows = len(data)

    # FIXME: iterate over number of rows
    for i in range(num_rows):
        objects_to_classify = data.iloc[i, 1:]
        label = data.iloc[i, 0]

        nn_distance = nn_location = 1000000.0
        nn_label = 0.0

        # FIXME: iterate over number of rows
        for j in range(num_rows):
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
    accuracy = correctly_classified / num_rows
    return accuracy


if __name__ == '__main__':
    cross_validation(pd.DataFrame(), [], 0)
