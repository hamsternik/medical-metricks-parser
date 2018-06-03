__author__ = 'khomitsevich'

import numpy as np

class DataProcessor:
    """ DataProcessor class """
    
    def __init__(self, data_list: list):
        self.data_list = data_list

    @property
    def get_average(self):
        return np.average(self.data_list)

    @property
    def get_std(self):
        return np.std(self.data_list)
