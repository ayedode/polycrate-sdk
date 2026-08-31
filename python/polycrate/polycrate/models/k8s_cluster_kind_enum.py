from typing import Literal

K8SClusterKindEnum = Literal["generic", "loopback", "polycrate"]

K8S_CLUSTER_KIND_ENUM_VALUES: set[K8SClusterKindEnum] = {
    "generic",
    "loopback",
    "polycrate",
}


def check_k8s_cluster_kind_enum(value: str) -> K8SClusterKindEnum:
    if value in K8S_CLUSTER_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_CLUSTER_KIND_ENUM_VALUES!r}")
