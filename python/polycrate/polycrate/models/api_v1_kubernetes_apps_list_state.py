from typing import Literal

ApiV1KubernetesAppsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_KUBERNETES_APPS_LIST_STATE_VALUES: set[ApiV1KubernetesAppsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_kubernetes_apps_list_state(value: str) -> ApiV1KubernetesAppsListState:
    if value in API_V1_KUBERNETES_APPS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_LIST_STATE_VALUES!r}")
