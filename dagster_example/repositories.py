"""Collection of Dagster repositories"""
from dagster import repository

from dagster_example.assets.cereal import cereals, highest_calorie_cereal, highest_protein_cereal
from dagster_example.jobs import complex_job, complex_job_with_fail, hello_cereal_job
from dagster_example.schedules import every_weekday_9am
from dagster_example.sensors import report_failure


@repository
def dagster_examples():
    """Collection of example jobs, assets, and schedules used by Dagster."""
    return [
        complex_job,
        hello_cereal_job,
        cereals,
        highest_calorie_cereal,
        highest_protein_cereal,
        every_weekday_9am,
        complex_job_with_fail,
        report_failure,
    ]
