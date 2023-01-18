from dagster import (
    RunFailureSensorContext,
    RunRequest,
    SkipReason,
    get_dagster_logger,
    make_email_on_run_failure_sensor,
    op,
    run_failure_sensor,
)

from dagster_example.reporting import PrometheusInfo, push_to_prometheus

# @run_failure_sensor(
#     monitor_all_repositories=True,
#     minimum_interval_seconds=30,
#     description="Dagster sensor for reporting job failures.",
#     request_job=push_to_prometheus,
# )
# def report_failure(context: RunFailureSensorContext):
#     run_config = {"ops": {"status_report": {"config": {"job_name": context.dagster_run.job_name}}}}
#     return RunRequest(run_key=None, run_config=run_config)


@run_failure_sensor
def report_failure(context: RunFailureSensorContext):
    fail_reason = context.failure_event.message
    fail_reason = "Unknown" if fail_reason is None else fail_reason
    pmi = PrometheusInfo(
        labels={
            "job_name": context.dagster_run.job_name,
            "sensor_name": context.sensor_name,
            "failure_event": fail_reason,
        }
    )
    push_to_prometheus(pmi)
