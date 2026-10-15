from typing import Literal

K8SAddonState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

K8S_ADDON_STATE_VALUES: set[K8SAddonState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_k8s_addon_state(value: str) -> K8SAddonState:
    if value in K8S_ADDON_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_ADDON_STATE_VALUES!r}")
