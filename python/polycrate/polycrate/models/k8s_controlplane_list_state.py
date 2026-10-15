from typing import Literal

K8SControlplaneListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

K8S_CONTROLPLANE_LIST_STATE_VALUES: set[K8SControlplaneListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_k8s_controlplane_list_state(value: str) -> K8SControlplaneListState:
    if value in K8S_CONTROLPLANE_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_CONTROLPLANE_LIST_STATE_VALUES!r}")
