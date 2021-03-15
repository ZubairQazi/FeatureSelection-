import pandas as pd
import random

from kfold import cross_validation


# TODO: Implement backward search

def forward_search(data):
    # set of features selected
    current_features = set()

    num_cols = len(data.columns)
    # iterate through each level
    for i in range(num_cols - 1):
        # store feature to add and best accuracy so far
        feature_to_add = None
        best_accuracy = 0

        print('On level {} of the search tree'.format(i + 1))
        # iterate through each feature
        for j in range(num_cols - 1):
            if j + 1 not in current_features:
                print('\tConsidering adding feature {}'.format(j + 1))
                accuracy = cross_validation(data, current_features, j + 1)

                # update best accuracy if improvement exists
                if accuracy > best_accuracy:
                    best_accuracy = accuracy
                    print('Updated Accuracy:', best_accuracy)
                    feature_to_add = j + 1

        current_features.add(feature_to_add)
        print('Feature {} added on level {}\n'.format(feature_to_add, i + 1))

    print('Best Accuracy:', best_accuracy)

    return 0


if __name__ == '__main__':
    input_data = pd.read_csv('data/CS170_small_special_testdata__95.txt', delim_whitespace=True, header=None)
    forward_search(input_data)
