from typing import Literal

PatchedEndpointRequestScope = Literal["system", "user"]

PATCHED_ENDPOINT_REQUEST_SCOPE_VALUES: set[PatchedEndpointRequestScope] = {
    "system",
    "user",
}


def check_patched_endpoint_request_scope(value: str) -> PatchedEndpointRequestScope:
    if value in PATCHED_ENDPOINT_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_ENDPOINT_REQUEST_SCOPE_VALUES!r}")
