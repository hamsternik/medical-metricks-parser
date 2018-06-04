__author__ = 'khomitsevich'

import metricks.excel_char_index_generator as excel_char_index_generator

RESULT_PARAM_COLUMN_LEADING_IND = 3
RESULT_PARAM_TITLES = ["DICE", "SPEC", "SENS", "ACCUR", "Time (w init)"]

class ResultWorkSheetDataProcessor:
    
    def __init__(self, result_worksheet, cell_title_prefix, metrics_dict_keys_full_sorted_list):
        self.result_worksheet = result_worksheet
        self.cell_title_prefix = cell_title_prefix
        self.metrics_dict_keys_full_sorted_list = metrics_dict_keys_full_sorted_list

    ### For each folder

    def calculate_average_and_std_of_dice(self, dice_indexes_dict, param_row_index: int = 2):
        self.__calculate_average_and_std_of_param(dice_indexes_dict, param_row_index)
    
    def calculate_average_and_std_of_spec(self, spec_indexes_dict, param_row_index: int = 3):
        self.__calculate_average_and_std_of_param(spec_indexes_dict, param_row_index)

    def calculate_average_and_std_of_sens(self, sens_indexes_dict, param_row_index: int = 4):
        self.__calculate_average_and_std_of_param(sens_indexes_dict, param_row_index)

    def calculate_average_and_std_of_accur(self, accur_indexes_dict, param_row_index: int = 5):
        self.__calculate_average_and_std_of_param(accur_indexes_dict, param_row_index)

    def calculate_average_and_std_of_time(self, time_indexes_dict, param_row_index: int = 6):
        self.__calculate_average_and_std_of_param(time_indexes_dict, param_row_index)

    ### Overall 

    def calculate_average_and_std_of_dice_overall(self, dice_indexes_dict, param_row_index: int = 2):
        self.__calculate_average_and_std_of_param_overall(dice_indexes_dict, param_row_index)
    
    def calculate_average_and_std_of_spec_overall(self, spec_indexes_dict, param_row_index: int = 3):
        self.__calculate_average_and_std_of_param_overall(spec_indexes_dict, param_row_index)

    def calculate_average_and_std_of_sens_overall(self, sens_indexes_dict, param_row_index: int = 4):
        self.__calculate_average_and_std_of_param_overall(sens_indexes_dict, param_row_index)

    def calculate_average_and_std_of_accur_overall(self, accur_indexes_dict, param_row_index: int = 5):
        self.__calculate_average_and_std_of_param_overall(accur_indexes_dict, param_row_index)

    def calculate_average_and_std_of_time_overall(self, time_indexes_dict, param_row_index: int = 6):
        self.__calculate_average_and_std_of_param_overall(time_indexes_dict, param_row_index)

    ### Private methods

    def __calculate_average_and_std_of_param(self, param_indexes_dict, param_row_index:int):
        for dir_path in self.metrics_dict_keys_full_sorted_list:
            average_excel_formulae = "=AVERAGE("
            std_excel_formulae = "=STDEV("
            for sens_ind_tuple in param_indexes_dict[dir_path]:
                """ Calculate average and standard deviation formulaes for a specific parameter. """
                result_index = excel_char_index_generator.get_excel_char_index_by_numeric(sens_ind_tuple[1]) + str(sens_ind_tuple[0])
                average_excel_formulae += f"{self.cell_title_prefix}{result_index},"
                std_excel_formulae += f"{self.cell_title_prefix}{result_index},"
            average_excel_formulae = average_excel_formulae[:len(average_excel_formulae) - 1] + ")"
            std_excel_formulae = std_excel_formulae[:len(std_excel_formulae) - 1] + ")"

            workseet_first_time_std_row_index = param_row_index + len(RESULT_PARAM_TITLES) + 1
            worksheet_first_time_col_index = RESULT_PARAM_COLUMN_LEADING_IND + self.metrics_dict_keys_full_sorted_list.index(dir_path) + 1
            
            self.result_worksheet.cell(param_row_index, worksheet_first_time_col_index, average_excel_formulae)
            self.result_worksheet.cell(workseet_first_time_std_row_index, worksheet_first_time_col_index, std_excel_formulae)
    # __calculate_average_and_std_of_param

    def __calculate_average_and_std_of_param_overall(self, param_indexes_dict, param_row_index:int):
        average_excel_formulae = "=AVERAGE("
        std_excel_formulae = "=STDEV("
        for dir_path in self.metrics_dict_keys_full_sorted_list:    
            for sens_ind_tuple in param_indexes_dict[dir_path]:
                """ Calculate average and standard deviation formulaes for a specific parameter. """
                result_index = excel_char_index_generator.get_excel_char_index_by_numeric(sens_ind_tuple[1]) + str(sens_ind_tuple[0])
                average_excel_formulae += f"{self.cell_title_prefix}{result_index},"
                std_excel_formulae += f"{self.cell_title_prefix}{result_index},"
        average_excel_formulae = average_excel_formulae[:len(average_excel_formulae) - 1] + ")"
        std_excel_formulae = std_excel_formulae[:len(std_excel_formulae) - 1] + ")"

        std_row_final_index = param_row_index + len(RESULT_PARAM_TITLES) + 1
        col_final_index = RESULT_PARAM_COLUMN_LEADING_IND - 1
            
        self.result_worksheet.cell(param_row_index, col_final_index, average_excel_formulae)
        self.result_worksheet.cell(std_row_final_index, col_final_index, std_excel_formulae)
    # __calculate_average_and_std_of_param_overall