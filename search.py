import pandas as np
import random

from kfold import cross_validation


def feature_search(features):
    # set of features selected
    current_features = set()

    # iterate through each level
    for i in range(len(features)):

        # store feature to add and best accuracy so far
        feature_to_add = 0
        best_accuracy = 0

        print('On level {} of the search tree'.format(i + 1))
        # iterate through each feature
        for j in range(len(features)):
            if j + 1 not in current_features:
                print('\tConsidering adding feature {}'.format(j + 1))
                accuracy = cross_validation(features, current_features, j + 1)

                # update best accuracy if improvement exists
                if accuracy > best_accuracy:
                    best_accuracy = accuracy
                    feature_to_add = j + 1

        current_features.add(feature_to_add)
        print('Feature {} added on level {}\n'.format(feature_to_add, i + 1))

    return 0


if __name__ == '__main__':
    input = [1, 2, 3, 4]
    feature_search(input)
