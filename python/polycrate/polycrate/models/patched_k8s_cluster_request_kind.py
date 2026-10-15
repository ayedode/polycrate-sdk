from typing import Literal

PatchedK8SClusterRequestKind = Literal["generic", "loopback", "polycrate"]

PATCHED_K8S_CLUSTER_REQUEST_KIND_VALUES: set[PatchedK8SClusterRequestKind] = {
    "generic",
    "loopback",
    "polycrate",
}


def check_patched_k8s_cluster_request_kind(value: str) -> PatchedK8SClusterRequestKind:
    if value in PATCHED_K8S_CLUSTER_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_K8S_CLUSTER_REQUEST_KIND_VALUES!r}")
