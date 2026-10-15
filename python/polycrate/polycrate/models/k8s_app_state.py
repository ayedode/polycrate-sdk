from typing import Literal

K8SAppState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

K8S_APP_STATE_VALUES: set[K8SAppState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_k8s_app_state(value: str) -> K8SAppState:
    if value in K8S_APP_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_APP_STATE_VALUES!r}")
