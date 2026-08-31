from typing import Literal

ApiV1KubernetesAddonsListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_KUBERNETES_ADDONS_LIST_STATE_NOT_VALUES: set[ApiV1KubernetesAddonsListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_kubernetes_addons_list_state_not(value: str) -> ApiV1KubernetesAddonsListStateNot:
    if value in API_V1_KUBERNETES_ADDONS_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_LIST_STATE_NOT_VALUES!r}")
