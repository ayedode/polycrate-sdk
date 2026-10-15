from typing import Literal

K8SClusterCriticalityType2Type1 = Literal["", "high", "low", "medium"]

K8S_CLUSTER_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[K8SClusterCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_k8s_cluster_criticality_type_2_type_1(value: str) -> K8SClusterCriticalityType2Type1:
    if value in K8S_CLUSTER_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_CLUSTER_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}")
