import re
from collections import Counter
from itertools import islice


class LogParser:
    def __init__(self, log_name):
        self.log_name = log_name



    def get_most_common(self, top):
        self.top = top
        with open(self.log_name, 'r') as read_file:
            data = read_file.read()
            ipaddr = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
            result = Counter(re.findall(ipaddr, data)).most_common(self.top)
            return result

    def log_by_http_code(self, output_file, code):
        self.output_file = output_file
        self.code = code
        with open(self.log_name, 'r') as read_file:
            with open(self.output_file, 'w') as write_file:
                for line in islice(read_file.readlines(), 1, None):
                    if line.split()[8] == self.code:
                        write_file.write(line)

