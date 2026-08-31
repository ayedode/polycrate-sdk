from typing import Literal

ApiV1KubernetesAppsListScope = Literal["system", "user"]

API_V1_KUBERNETES_APPS_LIST_SCOPE_VALUES: set[ApiV1KubernetesAppsListScope] = {
    "system",
    "user",
}


def check_api_v1_kubernetes_apps_list_scope(value: str) -> ApiV1KubernetesAppsListScope:
    if value in API_V1_KUBERNETES_APPS_LIST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_LIST_SCOPE_VALUES!r}")
