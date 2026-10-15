from typing import Literal

PatchedK8SControlplaneRequestKind = Literal["generic"]

PATCHED_K8S_CONTROLPLANE_REQUEST_KIND_VALUES: set[PatchedK8SControlplaneRequestKind] = {
    "generic",
}


def check_patched_k8s_controlplane_request_kind(value: str) -> PatchedK8SControlplaneRequestKind:
    if value in PATCHED_K8S_CONTROLPLANE_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_K8S_CONTROLPLANE_REQUEST_KIND_VALUES!r}")
