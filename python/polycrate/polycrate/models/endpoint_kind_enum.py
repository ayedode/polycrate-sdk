from typing import Literal

EndpointKindEnum = Literal["dns", "http", "icmp", "tcp"]

ENDPOINT_KIND_ENUM_VALUES: set[EndpointKindEnum] = {
    "dns",
    "http",
    "icmp",
    "tcp",
}


def check_endpoint_kind_enum(value: str) -> EndpointKindEnum:
    if value in ENDPOINT_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENDPOINT_KIND_ENUM_VALUES!r}")
