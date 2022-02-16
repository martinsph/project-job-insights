import csv
from functools import lru_cache


@lru_cache
def read(path):
    jobs_file = []
    with open(path) as file:
        read_job = csv.DictReader(file)
        for job in read_job:
            jobs_file.append(job)
    return jobs_file
