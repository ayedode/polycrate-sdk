from typing import Literal

K8SVolumeLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

K8S_VOLUME_LAST_STATE_VALUES: set[K8SVolumeLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_k8s_volume_last_state(value: str) -> K8SVolumeLastState:
    if value in K8S_VOLUME_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_VOLUME_LAST_STATE_VALUES!r}")
