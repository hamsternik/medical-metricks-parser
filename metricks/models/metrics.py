__author__ = 'khomitsevich'

ATTRIBUTES_COUNT: int = 14

class Metrics:
    """ Metrics data class. """

    # TODO: Initialization process should be more clearer, better to pass dict with keys as class parameter titles
    def __init__(self, filepath:str, filename:str, args:list):    
        self.__argument_count_validation(filepath, filename, args)
        self.__non_empty_arguments_validation(filepath, filename, args)
        
        self.name = filename
        self.step = float(args[0].replace(',', '.'))
        self.angel = float(args[1].replace(',', '.'))
        self.last_dots_count = float(args[2].replace(',', '.'))
        self.in_to_out_coef = float(args[3].replace(',', '.'))
        self.out_to_in_coef = float(args[4].replace(',', '.'))
        self.dice = float(args[5].replace(',', '.'))
        self.spec = float(args[6].replace(',', '.'))
        self.sens = float(args[7].replace(',', '.'))
        self.accu = float(args[8].replace(',', '.'))
        self.time_of_work_with_init = float(args[9].replace(',', '.'))
        self.time_of_work_wihout_init = float(args[10].replace(',', '.'))
        self.otsu_treshold = float(args[11].replace(',', '.'))
        self.average_in = float(args[12].replace(',', '.'))
        self.average_out = float(args[13].replace(',', '.'))

    def __repr__(self):
        return """Metrics: ('name': {self.name}, 'step': {self.step}, 'angel': {self.angel}, 
        'last_dots_count': {self.last_dots_count}, 'in_to_out_coef': {self.in_to_out_coef}, 
        'out_to_in_coef': {self.out_to_in_coef},  'dice': {self.dice}, 'spec': {self.spec}, 'sens': {self.sens}, 
        'accu': {self.accu},  'time_of_work_with_init': {self.time_of_work_with_init}, 
        'time_of_work_wihout_init': {self.time_of_work_wihout_init}, 'otsu_treshold': {self.otsu_treshold},
        'average_in': {self.average_in}, 'average_out': {self.average_out})
        """.format(self=self)

    def __str__(self):
        return self.__repr__

    def __argument_count_validation(self, filepath:str, filename:str, args:list):
        if len(args) != ATTRIBUTES_COUNT:
            error_message = f"WARNING: At instance '{filename}' on path '{filepath}' has been passed list with '{len(args)}' arguments, should be {ATTRIBUTES_COUNT}."
            print(error_message)
            raise ValueError(error_message)

    def __non_empty_arguments_validation(self, filepath:str, filename:str, args:list):
        for arg in args:
            if arg is None:
                error_message = f"WARNING: Found an empty argument at file: '{filename}' on path '{filepath}'."
                print(error_message)
                raise ValueError(error_message)
