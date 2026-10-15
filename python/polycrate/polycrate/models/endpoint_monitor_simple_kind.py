from typing import Literal

EndpointMonitorSimpleKind = Literal["uptime-kuma"]

ENDPOINT_MONITOR_SIMPLE_KIND_VALUES: set[EndpointMonitorSimpleKind] = {
    "uptime-kuma",
}


def check_endpoint_monitor_simple_kind(value: str) -> EndpointMonitorSimpleKind:
    if value in ENDPOINT_MONITOR_SIMPLE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENDPOINT_MONITOR_SIMPLE_KIND_VALUES!r}")
