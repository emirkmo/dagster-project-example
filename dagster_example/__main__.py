"""Example of how to run a Dagster op from normal Python script."""
from dagster_example.jobs import complex_job, complex_job_with_fail
from dagster_example.lifetime import start_prometheus

if __name__ == "__main__":
    # start_prometheus(9090)
    # result = complex_job.execute_in_process()
    result2 = complex_job_with_fail.execute_in_process()
