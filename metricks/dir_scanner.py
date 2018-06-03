__author__ = 'khomitsevich'

import os

CSV_FILENAME_TO_EXCLUDE = 'All metricks.csv'

class DirectoryScanner:
    def __init__(self, dirpath):
        self.dirpath = dirpath

    @property
    def filesDictToProcess(self):
        files_dict = {}
        for root_dir, _, files in os.walk(self.dirpath):
            csv_files = [csv_files for csv_files in files if not csv_files == CSV_FILENAME_TO_EXCLUDE and csv_files.endswith('.csv')]
            if len(csv_files) == 0:
                continue
            files_dict[root_dir] = csv_files
        return files_dict
