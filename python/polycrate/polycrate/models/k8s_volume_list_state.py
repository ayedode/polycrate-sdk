from typing import Literal

K8SVolumeListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

K8S_VOLUME_LIST_STATE_VALUES: set[K8SVolumeListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_k8s_volume_list_state(value: str) -> K8SVolumeListState:
    if value in K8S_VOLUME_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_VOLUME_LIST_STATE_VALUES!r}")
