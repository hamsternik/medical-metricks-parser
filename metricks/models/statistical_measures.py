__author__ = 'khomitsevich'

class StatisticalMeasures:
    """ StatisticalMeasures data class. """

    def __init__(self, average: float, sd: float):
        self.average = average
        self.sd = sd

    @property
    def description(self):
        return "StatisticalMeasures: ('average': " + str(self.average) +  ", 'sd' " + str(self.sd) + ")"

    def __repr__(self):
        return f"StatisticalMeasures: ('average': {self.average}, 'sd': {self.sd})"

    def __str__(self):
        return self.__repr__
