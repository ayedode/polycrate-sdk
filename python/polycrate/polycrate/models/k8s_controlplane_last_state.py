from typing import Literal

K8SControlplaneLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

K8S_CONTROLPLANE_LAST_STATE_VALUES: set[K8SControlplaneLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_k8s_controlplane_last_state(value: str) -> K8SControlplaneLastState:
    if value in K8S_CONTROLPLANE_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_CONTROLPLANE_LAST_STATE_VALUES!r}")
