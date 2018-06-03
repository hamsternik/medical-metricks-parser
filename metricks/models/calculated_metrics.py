__author__ = 'khomitsevich'

from metricks.models.statistical_measures import StatisticalMeasures

class CalculatedMetrics:
    """ CalculatedMetrics data class. 

    Attributes:
        metrics_ids (dict): Dictionary with:
            - key: should be a single in dictionary, equal to directory name
            - values: list of all metrics file titles
        dice (StatisticalMeasures): DICE metrics attribute 
        spec (StatisticalMeasures): SPEC metrics attribute 
        sens (StatisticalMeasures): SENS metrics attribute 
        accu (StatisticalMeasures): ACCU metrics attribute 
        time (StatisticalMeasures): Time of work (w/o Init) metrics attribute 
    """

    def __init__(
            self,
            metrics_directory: str,
            metrics_ids: dict, 
            dice: StatisticalMeasures, 
            spec: StatisticalMeasures, 
            sens: StatisticalMeasures, 
            accu: StatisticalMeasures, 
            time: StatisticalMeasures
        ):
        self.metrics_directory = metrics_directory
        self.metrics_ids = metrics_ids
        self.dice = dice
        self.spec = spec
        self.sens = sens
        self.accu = accu
        self.time = time

    def __repr__(self):
        return f""" 
        CalculatedMetrics: ('metrics_directory': {self.metrics_directory}, 
        'metrics_ids': {self.metrics_ids}, 'dice': {self.dice.description}, 
        'spec': {self.spec.description}, 'sens': {self.sens.description}, 
        'accu': {self.accu.description}, 'time': {self.time.description})
        """

    def __str__(self):
        return self.__repr__
