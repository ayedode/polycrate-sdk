from typing import Literal

EndpointListKind = Literal["dns", "http", "icmp", "tcp"]

ENDPOINT_LIST_KIND_VALUES: set[EndpointListKind] = {
    "dns",
    "http",
    "icmp",
    "tcp",
}


def check_endpoint_list_kind(value: str) -> EndpointListKind:
    if value in ENDPOINT_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENDPOINT_LIST_KIND_VALUES!r}")
