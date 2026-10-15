from typing import Literal

PatchedEndpointRequestKind = Literal["dns", "http", "icmp", "tcp"]

PATCHED_ENDPOINT_REQUEST_KIND_VALUES: set[PatchedEndpointRequestKind] = {
    "dns",
    "http",
    "icmp",
    "tcp",
}


def check_patched_endpoint_request_kind(value: str) -> PatchedEndpointRequestKind:
    if value in PATCHED_ENDPOINT_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_ENDPOINT_REQUEST_KIND_VALUES!r}")
