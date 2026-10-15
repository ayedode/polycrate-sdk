from typing import Literal

K8SAddonConfigRevisionLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

K8S_ADDON_CONFIG_REVISION_LAST_STATE_VALUES: set[K8SAddonConfigRevisionLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_k8s_addon_config_revision_last_state(value: str) -> K8SAddonConfigRevisionLastState:
    if value in K8S_ADDON_CONFIG_REVISION_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_ADDON_CONFIG_REVISION_LAST_STATE_VALUES!r}")
