from typing import Literal

PatchedK8SClusterRequestScope = Literal["system", "user"]

PATCHED_K8S_CLUSTER_REQUEST_SCOPE_VALUES: set[PatchedK8SClusterRequestScope] = {
    "system",
    "user",
}


def check_patched_k8s_cluster_request_scope(value: str) -> PatchedK8SClusterRequestScope:
    if value in PATCHED_K8S_CLUSTER_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_K8S_CLUSTER_REQUEST_SCOPE_VALUES!r}")
