from typing import Literal

K8SAddonLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

K8S_ADDON_LAST_STATE_VALUES: set[K8SAddonLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_k8s_addon_last_state(value: str) -> K8SAddonLastState:
    if value in K8S_ADDON_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_ADDON_LAST_STATE_VALUES!r}")
