from typing import Literal

K8SClusterKind = Literal["generic", "loopback", "polycrate"]

K8S_CLUSTER_KIND_VALUES: set[K8SClusterKind] = {
    "generic",
    "loopback",
    "polycrate",
}


def check_k8s_cluster_kind(value: str) -> K8SClusterKind:
    if value in K8S_CLUSTER_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_CLUSTER_KIND_VALUES!r}")
