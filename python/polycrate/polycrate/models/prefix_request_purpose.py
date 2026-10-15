from typing import Literal

PrefixRequestPurpose = Literal["controlplane", "loadbalancer"]

PREFIX_REQUEST_PURPOSE_VALUES: set[PrefixRequestPurpose] = {
    "controlplane",
    "loadbalancer",
}


def check_prefix_request_purpose(value: str) -> PrefixRequestPurpose:
    if value in PREFIX_REQUEST_PURPOSE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PREFIX_REQUEST_PURPOSE_VALUES!r}")
