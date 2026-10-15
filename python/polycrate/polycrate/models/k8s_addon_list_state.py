from typing import Literal

K8SAddonListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

K8S_ADDON_LIST_STATE_VALUES: set[K8SAddonListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_k8s_addon_list_state(value: str) -> K8SAddonListState:
    if value in K8S_ADDON_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_ADDON_LIST_STATE_VALUES!r}")
