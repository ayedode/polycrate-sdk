from typing import Literal

K8SClusterState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

K8S_CLUSTER_STATE_VALUES: set[K8SClusterState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_k8s_cluster_state(value: str) -> K8SClusterState:
    if value in K8S_CLUSTER_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_CLUSTER_STATE_VALUES!r}")
