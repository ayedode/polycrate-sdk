from typing import Literal

EndpointMonitorKindEnum = Literal["uptime-kuma"]

ENDPOINT_MONITOR_KIND_ENUM_VALUES: set[EndpointMonitorKindEnum] = {
    "uptime-kuma",
}


def check_endpoint_monitor_kind_enum(value: str) -> EndpointMonitorKindEnum:
    if value in ENDPOINT_MONITOR_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENDPOINT_MONITOR_KIND_ENUM_VALUES!r}")
