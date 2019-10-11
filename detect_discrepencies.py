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
    x = list(range(bucket_size))
    plt.scatter(x, bucket_totals, label='domains in bucket', color='b', marker=".")

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Distribution of domains in databases after crc32 hash being applied')
    plt.legend()
    plt.show()

def write_results_to_file(bucket_totals):
    with open('logs/quantity_results.txt', 'w') as f:
        for item in bucket_totals:
            f.write("%s\n" % item)

def write_discrepencies_log(message):
    with open('logs/discrepencies_log.txt', 'a') as f:
        f.write("%s\n" % message)

with open("data/majestic_million.csv") as csv_file:
   for row in csv.reader(csv_file, delimiter=','):
        for domain in row:
            python_crc32 = get_python_result(domain)
            golang_crc32 = get_python_result(domain)

            bucket_totals[int(golang_crc32)] += 1
            total += 1

            if (python_crc32 != golang_crc32):
                message = "crc32 discrepency on " + domain
            else:
                message ="crc32 for domain: " + domain + " (" + str(total) + ") is the same"

            write_discrepencies_log(message)

write_distribution_results(bucket_totals)
write_results_to_file(bucket_totals)
