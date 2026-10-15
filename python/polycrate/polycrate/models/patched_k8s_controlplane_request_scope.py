from typing import Literal

PatchedK8SControlplaneRequestScope = Literal["system", "user"]

PATCHED_K8S_CONTROLPLANE_REQUEST_SCOPE_VALUES: set[PatchedK8SControlplaneRequestScope] = {
    "system",
    "user",
}


def check_patched_k8s_controlplane_request_scope(value: str) -> PatchedK8SControlplaneRequestScope:
    if value in PATCHED_K8S_CONTROLPLANE_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_K8S_CONTROLPLANE_REQUEST_SCOPE_VALUES!r}")
