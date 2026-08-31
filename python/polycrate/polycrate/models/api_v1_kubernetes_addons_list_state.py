from typing import Literal

ApiV1KubernetesAddonsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_KUBERNETES_ADDONS_LIST_STATE_VALUES: set[ApiV1KubernetesAddonsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_kubernetes_addons_list_state(value: str) -> ApiV1KubernetesAddonsListState:
    if value in API_V1_KUBERNETES_ADDONS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_LIST_STATE_VALUES!r}")
