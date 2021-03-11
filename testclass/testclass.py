from glob import glob
from os.path import (join, isfile, splitext)


def load_json(file_name):
    import json
    with open(file_name, 'r') as f:
        return json.load(f)
    return None


def load_text(file_name):
    with open(file_name, 'r') as f:
        return f.read()
    return None


class TestClass:
    def __init__(self, dir_name, test_name):
        self.__dir_name = dir_name
        self.__test_name = test_name
        self.__expected_result = None
        self.__send_request = None
        self.__variables = None

    def get_test_name(self):
        return self.__test_name

    def get_expected_result(self):
        return self.__expected_result

    def get_send_request(self):
        return self.__send_request

    def get_dir_name(self):
        return self.__dir_name

    def get_variables(self):
        return self.__variables

    def load_files(self):
        for file in glob(join(self.__dir_name, self.__test_name, '*')):
            if isfile(file):
                file_name, file_ext = splitext(file)
                if 'json' in file_ext:
                    temp = load_json(file)

                if 'txt' in file_ext:
                    temp = load_text(file)

                if 'expected' in file_name:
                    self.__expected_result = temp

                if 'send' in file_name:
                    self.__send_request = temp

                if 'variables' in file_name:
                    self.__variables = temp

