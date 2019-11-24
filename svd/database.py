import numpy
import pandas

from .config import rating_dataset


def load(filepath, column):
    """
    Reads a binary file to load dataset.
    :param
        file path 
        column Used to label the dataframe
    :return
        Pandas.Dataframe Contains the dataset.
    """
    with open(filepath, 'r', encoding='ISO-8859-1') as f:
        text = str(f.read()).strip().split('\n')
        return pandas.DataFrame.from_records(
            [sentence.split('::') for sentence in text], columns=column)


def preprocess():
    """Wrapper function which loads dataset, preprocesses it and
    also assigns missing values to the sparse matrix

    :return
            utility_matrix numpy.ndarray containing the matrix
                                       representation of the dataset
    """
    dataset = load(rating_dataset,
                   column=['uid', 'mid', 'rating', 'time'])
    dataset.drop(labels=["time"], axis=1, inplace=True)
    dataset = dataset.astype(int)

    num_users = list(dataset['uid'].unique())
    num_users.sort()

    num_movies = list(dataset['mid'].unique())
    num_movies.sort()

    utility_matrix = numpy.full((len(num_users), len(num_movies)), 0)

    for iter in dataset.index:
        user_index = num_users.index(dataset['uid'][iter])
        movie_index = num_movies.index(dataset['mid'][iter])
        utility_matrix[user_index][movie_index] = dataset['rating'][iter]


    return utility_matrix
