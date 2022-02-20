from src.jobs import read


def get_unique_job_types(path):
    jobs_file = read(path)
    job_types = set()
    for job in jobs_file:
        job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    jobs_filtered_by_job_type = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_filtered_by_job_type.append(job)
    return jobs_filtered_by_job_type


def get_unique_industries(path):
    jobs_file = read(path)
    job_industries = set()
    for job in jobs_file:
        if job["industry"]:
            job_industries.add(job["industry"])
    return job_industries


def filter_by_industry(jobs, industry):
    jobs_filtered_by_industry = []
    for job in jobs:
        if job["industry"] == industry:
            jobs_filtered_by_industry.append(job)
    return jobs_filtered_by_industry


def get_max_salary(path):
    jobs_file = read(path)
    max_salary = 0
    for job in jobs_file:
        if job["max_salary"] and job["max_salary"].isnumeric():
            job_salary = int(job["max_salary"])
            if job_salary > max_salary:
                max_salary = job_salary
    return max_salary


def get_min_salary(path):
    jobs_file = read(path)
    min_salary = 100000
    for job in jobs_file:
        if job["min_salary"] and job["min_salary"].isnumeric():
            job_salary = int(job["min_salary"])
            if job_salary < min_salary:
                min_salary = job_salary
    return min_salary
    pass


def validation(job):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("max or/and min salary column do not exist")
    elif job["min_salary"] is None or job["max_salary"] is None:
        raise ValueError("max or/and min salary column do not exist")
    elif not isinstance(job["min_salary"], int):
        raise ValueError("min salary is not int")
    elif not isinstance(job["max_salary"], int):
        raise ValueError("max_salary is not int")


def matches_salary_range(job, salary):
    validation(job)
    if salary >= job["min_salary"] and salary <= job["max_salary"]:
        return True
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("min salary higher than max_salary")
    elif not isinstance(salary, int):
        raise ValueError("Salary is not int")
    # print(job["min_salary"], job["max_salary"], salary)
    return False


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
