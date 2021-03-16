import random
import sys
import numpy as np
from copy import deepcopy


def cross_validation(complete_data, current_features, feature_to_add):

    data = deepcopy(complete_data)
    for i in range(1, complete_data.shape[1]):
        if i not in current_features and i != feature_to_add:
            data[:, i] = 0

    correctly_classified = 0
    num_rows = data.shape[0]

    for i in range(num_rows):
        objects_to_classify = data[i, 1:]
        label = data[i, 0]

        nn_distance = nn_location = 10000.0
        nn_label = 0.0

        for j in range(num_rows):
            if i != j:
                # print('Ask if {} is nearest neighbors with {}'.format(i+1, j+1))
                distance = np.sqrt(sum(pow(objects_to_classify - data[j, 1:], 2)))
                if distance <= nn_distance:
                    nn_distance = distance
                    nn_location = j
                    nn_label = data[nn_location, 0]

        if label == nn_label:
            correctly_classified += 1

        # print('Object {} is in class {}'.format(i+1, label))
        # print('Its nearest neighbor is {} which is in class {}'.format(nn_location, nn_label))

    accuracy = correctly_classified / num_rows
    return accuracy


if __name__ == '__main__':
    cross_validation([], [], 0)
