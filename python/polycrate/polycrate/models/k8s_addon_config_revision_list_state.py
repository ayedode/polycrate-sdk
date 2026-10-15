from typing import Literal

K8SAddonConfigRevisionListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

K8S_ADDON_CONFIG_REVISION_LIST_STATE_VALUES: set[K8SAddonConfigRevisionListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_k8s_addon_config_revision_list_state(value: str) -> K8SAddonConfigRevisionListState:
    if value in K8S_ADDON_CONFIG_REVISION_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_ADDON_CONFIG_REVISION_LIST_STATE_VALUES!r}")
