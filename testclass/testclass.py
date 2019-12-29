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
        self._dir_name = dir_name
        self._test_name = test_name
        self._expected_result = None
        self._send_request = None

    def load_files(self):
        for file in glob(join(self._dir_name, self._test_name, '*')):
            if isfile(file):
                file_name, file_ext = splitext(file)
                if 'json' in file_ext:
                    temp = load_json(file)

                if 'txt' in file_ext:
                    temp = load_text(file)

                if 'expected' in file_name:
                    self._expected_result = temp

                if 'send' in file_name:
                    self._send_request = temp
