from typing import Literal

K8SAppLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

K8S_APP_LAST_STATE_VALUES: set[K8SAppLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_k8s_app_last_state(value: str) -> K8SAppLastState:
    if value in K8S_APP_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_APP_LAST_STATE_VALUES!r}")
