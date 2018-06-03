__author__ = 'khomitsevich'

import os
import pprint

from metricks.csv_data_parser import CSVDataParser

def get_metricks_dict(files_dict: dict = None):
    metricks_dict = {}
    for key, values in files_dict.items():
        metrics_list = []
        for value in values:
            # pprint.pprint("=== DIRECTORY: {}/{} ===".format(key, value)) ### DEBUG
            csv_data_processor = CSVDataParser(os.path.join(key, value))
            metrics_model = csv_data_processor.parseCSVRawDataIntoMetrics(key, value)
            if metrics_model is not None:
                metrics_list.append(metrics_model)
        metricks_dict[key] = metrics_list
    return metricks_dict

def get_metricks_dict_keys_sorted_list(metricks_dict: dict = None):
    metricks_dict_keys_sorted_list = []
    for key in metricks_dict.keys():
        last_slash_occur = str(key).rfind('/')
        metrics_folder_title = key[last_slash_occur+1:]
        metricks_dict_keys_sorted_list.append(metrics_folder_title)
    metricks_dict_keys_sorted_list.sort()
    return metricks_dict_keys_sorted_list

def get_max_metricks_number_overall(metricks_dict: dict = None):
    biggest_metricks_number = -1
    for key in metricks_dict.keys():
        biggest_metricks_number = max(biggest_metricks_number, len(metricks_dict[key]))
    return biggest_metricks_number
