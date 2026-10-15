from typing import Literal

K8SClusterScope = Literal["system", "user"]

K8S_CLUSTER_SCOPE_VALUES: set[K8SClusterScope] = {
    "system",
    "user",
}


def check_k8s_cluster_scope(value: str) -> K8SClusterScope:
    if value in K8S_CLUSTER_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_CLUSTER_SCOPE_VALUES!r}")
