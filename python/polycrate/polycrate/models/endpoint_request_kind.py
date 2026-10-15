from typing import Literal

EndpointRequestKind = Literal["dns", "http", "icmp", "tcp"]

ENDPOINT_REQUEST_KIND_VALUES: set[EndpointRequestKind] = {
    "dns",
    "http",
    "icmp",
    "tcp",
}


def check_endpoint_request_kind(value: str) -> EndpointRequestKind:
    if value in ENDPOINT_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENDPOINT_REQUEST_KIND_VALUES!r}")
