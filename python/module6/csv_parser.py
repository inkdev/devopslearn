import csv


class CsvParser():
    def __init__(self, file_name):
        self.file_name = file_name

    def get_country_profit(self, country):
        self.country = country
        with open(self.file_name, 'r') as readable:
            reader = csv.reader(readable)
            profit = 0
            for row in reader:
                if row[1] == self.country:
                    profit = profit + float(row[13])
            return round(profit, 2)

    def save_as(self, new_file_name, delimiter):
        self.new_file_name = new_file_name
        self.delimiter = delimiter
        with open(self.file_name, 'r') as readable:
            with open(self.new_file_name, 'w') as writable:
                reader = csv.reader(readable)
                writer = csv.writer(writable, delimiter=self.delimiter)
                for line in reader:
                    writer.writerow(line)

    def sell_over(self, item_type: str, threshold: int):
        self.item_type = str(item_type)
        self.threshold = int(threshold)
        with open(self.file_name, 'r') as readable:
            reader = csv.DictReader(readable)
            countries = []
            for row in reader:
                if row['Item Type'] == self.item_type and float(row['Units Sold']) > self.threshold:
                    countries.append(row['Country'])
        return sorted(set(countries))
