import os
import csv
import subprocess

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('TkAgg')

bucket_size = 64
total = 0
bucket_totals = [0] * bucket_size

def get_python_result(domain):
    command = 'python python-md5.py ' + domain
    domain_hash_result = os.popen(command).read()
    domain_hash_result = domain_hash_result.strip()
    return (domain_hash_result)

def get_golang_result(domain):
    command = 'java md5Experiment ' + domain
    domain_hash_result = os.popen(command).read()
    domain_hash_result = domain_hash_result.strip()
    return (domain_hash_result)

def write_distribution_results(bucket_totals):
    print("writing distribution results")
    x = list(range(bucket_size))
    plt.scatter(x, bucket_totals, label='domains in bucket', color='b', marker=".")

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Distribution of domains in databases after md5 hash being applied')
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
            python_md5 = get_python_result(domain)
            golang_md5 = get_python_result(domain)

            bucket_totals[int(golang_md5)] += 1
            total += 1

            if (python_md5 != golang_md5):
                message = "md5 discrepency on " + domain
            else:
                message ="md5 for domain: " + domain + " (" + str(total) + ") is the same"

            write_discrepencies_log(message)

write_distribution_results(bucket_totals)
write_results_to_file(bucket_totals)
