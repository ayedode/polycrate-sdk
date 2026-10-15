from typing import Literal

K8SVolumeState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

K8S_VOLUME_STATE_VALUES: set[K8SVolumeState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_k8s_volume_state(value: str) -> K8SVolumeState:
    if value in K8S_VOLUME_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_VOLUME_STATE_VALUES!r}")
