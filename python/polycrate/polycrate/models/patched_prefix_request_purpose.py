from typing import Literal

PatchedPrefixRequestPurpose = Literal["controlplane", "loadbalancer"]

PATCHED_PREFIX_REQUEST_PURPOSE_VALUES: set[PatchedPrefixRequestPurpose] = {
    "controlplane",
    "loadbalancer",
}


def check_patched_prefix_request_purpose(value: str) -> PatchedPrefixRequestPurpose:
    if value in PATCHED_PREFIX_REQUEST_PURPOSE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_PREFIX_REQUEST_PURPOSE_VALUES!r}")
