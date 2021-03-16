import pandas as pd
from copy import deepcopy
from kfold import cross_validation


def backward_elimination(data):
    # set of features selected
    current_features = set([feature for feature in range(1, data.shape[1])])

    # dictionary to track subsets of feature performances
    feature_performances = {}
    # stores accuracies at each iteration
    accuracies = set()
    # stores the accuracy with all features
    overall_accuracy = 0

    num_cols = data.shape[1]
    # iterate through each level
    for i in range(num_cols - 1):
        # store feature to add and best accuracy so far
        feature_to_remove = None
        best_accuracy = 0

        print('On level {} of the search tree'.format(i + 1))
        # iterate through each feature
        for j in range(num_cols - 1):
            if j + 1 in current_features:
                print('\tConsidering removing feature {}'.format(j + 1))

                sub_features = deepcopy(current_features)
                sub_features.remove(j + 1)
                accuracy = cross_validation(data, sub_features, 0)

                if i == 0 and j == 0:
                    overall_accuracy = accuracy

                # update best accuracy if improvement exists
                if accuracy > best_accuracy:
                    best_accuracy = accuracy
                    print('Updated Accuracy:', best_accuracy)
                    feature_to_remove = j + 1

                # keeps track of accuracies
                accuracies.add(best_accuracy)

        current_features.remove(feature_to_remove)

        # keep track of feature sets and corresponding accuracies
        if round(best_accuracy, 3) not in feature_performances.keys():
            feature_performances[round(best_accuracy, 3)] = deepcopy(current_features)

        print('Feature {} removed on level {}\n'.format(feature_to_remove, i + 1))

    print('Best Features: ', feature_performances[round(max(accuracies), 3)])
    print('Best Accuracy: ', round(max(accuracies), 3))
    print('Accuracy w/ All Features:', overall_accuracy)


def forward_selection(data):
    # set of features selected
    current_features = set()

    # dictionary to track subsets of feature performances
    feature_performances = {}
    accuracies = set()

    num_cols = data.shape[1]
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

                # keeps track of accuracies
                accuracies.add(best_accuracy)

        current_features.add(feature_to_add)
        # keep track of feature sets and corresponding accuracies
        if round(best_accuracy, 3) not in feature_performances.keys():
            feature_performances[round(best_accuracy, 3)] = deepcopy(current_features)
        print('Feature {} added on level {}\n'.format(feature_to_add, i + 1))

    print('Best Features: ', feature_performances[round(max(accuracies), 3)])
    print('Best Accuracy: ', round(max(accuracies), 3))
    print('Accuracy w/ All Features:', best_accuracy)


if __name__ == '__main__':

    print('Welcome to Zubair\'s Feature Selection Algorithm')

    file_name = input('Enter the input file name: ')
    input_data = pd.read_csv(file_name, delim_whitespace=True, header=None).values

    algorithm = input('Enter the algorithm you wish to run: \n\t 1. Forward Selection \n\t 2. Backward Elimination\n')

    if algorithm == '1':
        forward_selection(input_data)
    elif algorithm == '2':
        backward_elimination(input_data)
    else:
        print('Invalid options inputted!')
