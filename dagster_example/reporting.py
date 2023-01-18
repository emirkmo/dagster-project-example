# what is currently required
from dataclasses import dataclass, field

from dagster import Nothing, build_resources, op
from dagster_prometheus import prometheus_resource
from prometheus_client.metrics import Info


@dataclass
class PrometheusInfo:
    name: str = "failed_job"
    docs: str = "Info of failed Dagster job"
    labels: dict[str, str] = field(default_factory=dict)


# @Todo: Convert to OP that is provided Prometheus resource (Dependency injection)
def push_to_prometheus(prom_info: PrometheusInfo) -> Nothing:
    with build_resources({"prometheus": prometheus_resource}) as resources:
        prometheus = resources.prometheus  # type: ignore

        info = Info(prom_info.name, prom_info.docs, registry=prometheus.registry)
        info.info(prom_info.labels)
        prometheus.push_to_gateway("dagster_prom")
