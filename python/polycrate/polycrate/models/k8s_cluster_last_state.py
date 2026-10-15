from typing import Literal

K8SClusterLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

K8S_CLUSTER_LAST_STATE_VALUES: set[K8SClusterLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_k8s_cluster_last_state(value: str) -> K8SClusterLastState:
    if value in K8S_CLUSTER_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_CLUSTER_LAST_STATE_VALUES!r}")
