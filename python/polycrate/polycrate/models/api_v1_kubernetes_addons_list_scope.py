from typing import Literal

ApiV1KubernetesAddonsListScope = Literal["system", "user"]

API_V1_KUBERNETES_ADDONS_LIST_SCOPE_VALUES: set[ApiV1KubernetesAddonsListScope] = {
    "system",
    "user",
}


def check_api_v1_kubernetes_addons_list_scope(value: str) -> ApiV1KubernetesAddonsListScope:
    if value in API_V1_KUBERNETES_ADDONS_LIST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_LIST_SCOPE_VALUES!r}")
