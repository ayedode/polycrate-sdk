from typing import Literal

EndpointSimpleKind = Literal["dns", "http", "icmp", "tcp"]

ENDPOINT_SIMPLE_KIND_VALUES: set[EndpointSimpleKind] = {
    "dns",
    "http",
    "icmp",
    "tcp",
}


def check_endpoint_simple_kind(value: str) -> EndpointSimpleKind:
    if value in ENDPOINT_SIMPLE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENDPOINT_SIMPLE_KIND_VALUES!r}")
