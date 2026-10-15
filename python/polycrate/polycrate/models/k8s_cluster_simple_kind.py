from typing import Literal

K8SClusterSimpleKind = Literal["generic", "loopback", "polycrate"]

K8S_CLUSTER_SIMPLE_KIND_VALUES: set[K8SClusterSimpleKind] = {
    "generic",
    "loopback",
    "polycrate",
}


def check_k8s_cluster_simple_kind(value: str) -> K8SClusterSimpleKind:
    if value in K8S_CLUSTER_SIMPLE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_CLUSTER_SIMPLE_KIND_VALUES!r}")
