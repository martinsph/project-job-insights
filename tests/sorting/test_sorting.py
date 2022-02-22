# from src.sorting import sort_by
from src.sorting import sort_by


mock_jobs_list = [
    {"min_salary": 500, "max_salary": 3000, "date_posted": "2022-06-26"},
    {"min_salary": 5005, "max_salary": 305, "date_posted": "2023-06-26"},
    {"min_salary": 1000, "max_salary": 100, "date_posted": "2024-06-26"},
    {"min_salary": 105, "max_salary": 1005, "date_posted": "2025-06-26"},
]

mock_jobs_list_ordered_by_min_salary = [
    {"min_salary": 105, "max_salary": 1005, "date_posted": "2025-06-26"},
    {"min_salary": 500, "max_salary": 3000, "date_posted": "2022-06-26"},
    {"min_salary": 1000, "max_salary": 100, "date_posted": "2024-06-26"},
    {"min_salary": 5005, "max_salary": 305, "date_posted": "2023-06-26"},
]

mock_jobs_list_ordered_by_max_salary = [
    {"min_salary": 500, "max_salary": 3000, "date_posted": "2022-06-26"},
    {"min_salary": 105, "max_salary": 1005, "date_posted": "2025-06-26"},
    {"min_salary": 5005, "max_salary": 305, "date_posted": "2023-06-26"},
    {"min_salary": 1000, "max_salary": 100, "date_posted": "2024-06-26"},
]

mock_jobs_list_ordered_by_date_posted = [
    {"min_salary": 105, "max_salary": 1005, "date_posted": "2025-06-26"},
    {"min_salary": 1000, "max_salary": 100, "date_posted": "2024-06-26"},
    {"min_salary": 5005, "max_salary": 305, "date_posted": "2023-06-26"},
    {"min_salary": 500, "max_salary": 3000, "date_posted": "2022-06-26"},
]


def test_sort_by_criteria():
    sort_by(mock_jobs_list, "min_salary")
    assert mock_jobs_list == mock_jobs_list_ordered_by_min_salary

    sort_by(mock_jobs_list, "max_salary")
    assert mock_jobs_list == mock_jobs_list_ordered_by_max_salary

    sort_by(mock_jobs_list, "date_posted")
    assert mock_jobs_list == mock_jobs_list_ordered_by_date_posted
    pass
