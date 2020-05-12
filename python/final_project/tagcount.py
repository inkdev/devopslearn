import boto3
import requests
from bs4 import BeautifulSoup
from collections import defaultdict
from datetime import datetime
import sys


class CountTag:
    def __init__(self, url):
        self.url = requests.get(url)
        self.soup = BeautifulSoup(self.url.text, 'lxml')

    def total_tags(self):
        count = 0
        for tag in self.soup.find_all():
            count += 1
        return count

    def count_via_tag(self):
        mtch = defaultdict(int)
        for tag in self.soup.find_all():
            mtch[tag.name] += 1
        return dict(mtch)

    @property
    def result_tag(self):
        return f"{datetime.now().strftime('%Y/%m/%d %H:%M:%S')} {self.url.url} {self.total_tags()} {self.count_via_tag()}"

    def writelog(self, logfile):
        self.logfile=logfile
        timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        with open(self.logfile, 'a') as writable:
            log_string = f"{timestamp} {self.url.url} {self.total_tags()} {self.count_via_tag()}\n"
            writable.write(log_string)
        return [self.logfile, log_string]

    def upload_file(self, bucket_name):
        self.bucket_name = bucket_name
        s3 = boto3.resource('s3')
        s3.meta.client.upload_file(self.logfile, self.bucket_name, self.logfile)

if __name__ == '__main__':

    if len(sys.argv) < 4:
        print('You need 3 arguments: url, logname , s3bucket name')
        sys.exit()

    else:

        page = str(sys.argv[1])
        logname = str(sys.argv[2])
        bucketname = str(sys.argv[3])

        countTags = CountTag(page)
        print(countTags.result_tag)

        if logname and bucketname:
            countTags.writelog(logname)
            countTags.upload_file(bucketname)

        elif logname:
            countTags.writelog(logname)
        elif bucketname:
            countTags.upload_file(bucketname)

#test = CountTag('https://www.w3resource.com')
#print(test.total_tags())
#print(test.count_via_tag())
#test.writelog('CountTags.log')
#test.upload_file('bogdanov-310320')



