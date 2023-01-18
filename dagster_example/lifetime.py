from prometheus_client import start_http_server


def start_prometheus(port: int) -> None:
    return start_http_server(port)
