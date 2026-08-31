from typing import Literal

ApiV1KubernetesAppsListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_KUBERNETES_APPS_LIST_STATE_NOT_VALUES: set[ApiV1KubernetesAppsListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_kubernetes_apps_list_state_not(value: str) -> ApiV1KubernetesAppsListStateNot:
    if value in API_V1_KUBERNETES_APPS_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_LIST_STATE_NOT_VALUES!r}")
