import pandas as np
import random

def feature_search(features):

    current_features = set()
    for i in range(len(features)):
        feature_to_add = []
        best_accuracy = 0

        print('On level {} of the search tree'.format(i + 1))
        for j in range(len(features)):
            if j + 1 not in current_features:
                print('\tConsidering adding feature {}'.format(j + 1))
                accuracy = cross_validation(features, current_features, j + 1)

                if accuracy > best_accuracy:
                    best_accuracy = accuracy
                    feature_to_add = j + 1

        current_features.add(feature_to_add)
        print('Feature {} added on level {}\n'.format(feature_to_add, i + 1))

    return 0


def cross_validation(feature, current_features, idx):
    return random.randint(1, 10)


if __name__ == '__main__':
    input = [1, 2, 3, 4]
    feature_search(input)
