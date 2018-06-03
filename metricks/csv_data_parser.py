__author__ = 'khomitsevich'

import csv
import re
import pprint

from metricks.models.metrics import Metrics

FLOATING_RE = r"[+-]? *(?:\d+(?:[\.\,]\d*)?|[\.\,]\d+)(?:[eE][+-]?\d+)?"
CSV_DELIMITER = ';'
QUOTE_CHARACTER = '|'

class CSVDataParser:
    """ CSVDataProcessor class to read data from .csv file and parse regarding according format """
    
    def __init__(self, filepath):
        self.absolute_filepath = filepath

    def parseCSVRawDataIntoMetrics(self, metrics_filepath:str, metrics_filename:str):
        metrics_parsed_fields = []
        with open(self.absolute_filepath, newline='') as metrics_csv:
            csv_file = csv.reader(metrics_csv, delimiter=CSV_DELIMITER, quotechar=QUOTE_CHARACTER)
            for row in csv_file:
                if self.__isValidElementInListOfMetricsFileRow(row):
                    row_result = self.__getFloatValueFromMetricsFileRow(row)
                    metrics_parsed_fields.append(row_result)
                    # pprint.pprint(' | '.join(row)) ### DEBUG
                    # pprint.pprint(row_result) ### DEBUG
        try:
            metrics = Metrics(metrics_filepath, metrics_filename, metrics_parsed_fields)
            return self.__filterMetricsByDICEAsReturnedValue(metrics)
        except ValueError:
            # raise ValueError("Some problems have been occurred due to the parsing csv and creating instance with data.")
            # TODO: Should be handler more correctly
            return None

    def __getFloatValueFromMetricsFileRow(self, list_row: list):
        for element in list_row:
            result_list = re.findall(FLOATING_RE, element)
            if len(result_list) != 0:
                return result_list[0]
        return None


    def __isValidElementInListOfMetricsFileRow(self, list_row: list):
        if len(list_row) == 0:
            return False
        for element in list_row:
            if "Parameters" in element or "Results" in element or ((str)(element)).isspace():
                return False
        return True
    
    def __filterMetricsByDICEAsReturnedValue(self, metrics: Metrics):
        return metrics if metrics.dice > 0 else None
