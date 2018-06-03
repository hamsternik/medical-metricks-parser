__author__ = 'khomitsevich'

from metricks.data_processor import DataProcessor
from metricks.models.calculated_metrics import CalculatedMetrics
from metricks.models.statistical_measures import StatisticalMeasures

def get_calculated_metricks(metricks_dict: dict):
    calculated_metrics_dict = {}
    for dir_path in metricks_dict:
        # pprint.pprint("=== {} ===".format(dir_path)) ### DEBUG
        filename_list = [metricks_model_value.name for metricks_model_value in metricks_dict[dir_path]]
        dice_list = [metricks_model_value.dice for metricks_model_value in metricks_dict[dir_path]]
        spec_list = [metricks_model_value.spec for metricks_model_value in metricks_dict[dir_path]]
        sens_list = [metricks_model_value.sens for metricks_model_value in metricks_dict[dir_path]]
        accu_list = [metricks_model_value.accu for metricks_model_value in metricks_dict[dir_path]]
        time_list = [metricks_model_value.time_of_work_wihout_init for metricks_model_value in metricks_dict[dir_path]]

        dice_data_processor = DataProcessor(dice_list)
        spec_data_processor = DataProcessor(spec_list)
        sens_data_processor = DataProcessor(sens_list)
        accu_data_processor = DataProcessor(accu_list)
        time_data_processor = DataProcessor(time_list)

        calculated_metrics = CalculatedMetrics(
                                dir_path,
                                {dir_path: filename_list}, 
                                StatisticalMeasures(dice_data_processor.get_average, dice_data_processor.get_std),
                                StatisticalMeasures(spec_data_processor.get_average, spec_data_processor.get_std),
                                StatisticalMeasures(sens_data_processor.get_average, sens_data_processor.get_std),
                                StatisticalMeasures(accu_data_processor.get_average, accu_data_processor.get_std),
                                StatisticalMeasures(time_data_processor.get_average, time_data_processor.get_std))
        calculated_metrics_dict[dir_path] = calculated_metrics
    return calculated_metrics_dict
