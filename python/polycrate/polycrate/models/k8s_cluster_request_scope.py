from typing import Literal

K8SClusterRequestScope = Literal["system", "user"]

K8S_CLUSTER_REQUEST_SCOPE_VALUES: set[K8SClusterRequestScope] = {
    "system",
    "user",
}


def check_k8s_cluster_request_scope(value: str) -> K8SClusterRequestScope:
    if value in K8S_CLUSTER_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_CLUSTER_REQUEST_SCOPE_VALUES!r}")
