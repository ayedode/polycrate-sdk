from typing import Literal

K8SControlplaneState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

K8S_CONTROLPLANE_STATE_VALUES: set[K8SControlplaneState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_k8s_controlplane_state(value: str) -> K8SControlplaneState:
    if value in K8S_CONTROLPLANE_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_CONTROLPLANE_STATE_VALUES!r}")
