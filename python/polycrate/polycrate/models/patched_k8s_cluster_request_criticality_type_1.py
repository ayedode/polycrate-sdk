from typing import Literal

PatchedK8SClusterRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PATCHED_K8S_CLUSTER_REQUEST_CRITICALITY_TYPE_1_VALUES: set[PatchedK8SClusterRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_k8s_cluster_request_criticality_type_1(value: str) -> PatchedK8SClusterRequestCriticalityType1:
    if value in PATCHED_K8S_CLUSTER_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_K8S_CLUSTER_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
