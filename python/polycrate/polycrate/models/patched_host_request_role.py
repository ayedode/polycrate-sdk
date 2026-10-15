from typing import Literal

PatchedHostRequestRole = Literal["", "generic", "k8s-controlplane", "k8s-worker"]

PATCHED_HOST_REQUEST_ROLE_VALUES: set[PatchedHostRequestRole] = {
    "",
    "generic",
    "k8s-controlplane",
    "k8s-worker",
}


def check_patched_host_request_role(value: str) -> PatchedHostRequestRole:
    if value in PATCHED_HOST_REQUEST_ROLE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_HOST_REQUEST_ROLE_VALUES!r}")
