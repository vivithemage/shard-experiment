import os
import csv
import subprocess

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

bucket_size = 8192
total = 0
bucket_totals = [0] * bucket_size

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

def write_distribution_results(bucket_totals):
    print("writing distribution results")
    plt.plot(bucket_totals)
    plt.show()

with open("data/majestic_million.csv") as csv_file:
   for row in csv.reader(csv_file, delimiter=','):
        for domain in row:
            python_crc32 = get_python_result(domain)
            golang_crc32 = get_python_result(domain)

            bucket_totals[int(golang_crc32)] += 1
            total += 1

            if (python_crc32 != golang_crc32):
                print ("crc32 discrepency on " + domain)
            else:
                print ("crc32 for domain: " + domain + " (" + str(total) + ") is the same")

write_distribution_results(bucket_totals)
