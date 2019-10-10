import os
import csv
import subprocess

def get_python_result(domain):
    command = 'python python-crc32.py ' + domain
    domain_crc_result = os.popen(command).read()
    domain_crc_result = domain_crc_result.strip()
    return (domain_crc_result)

def get_golang_result(domain):
    command = 'go run golang-crc32.go ' + domain
    domain_crc_result = os.popen(command).read()
    domain_crc_result = domain_crc_result.strip()
    return (domain_crc_result)


with open("data/majestic_million.csv") as csv_file:
   for row in csv.reader(csv_file, delimiter=','):
        for domain in row:
            python_crc32 = get_python_result(domain)
            golang_crc32 = get_python_result(domain)
            
            if (python_crc32 != golang_crc32):
                print ("crc32 discrepency on " + domain)
