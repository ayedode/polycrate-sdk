from typing import Literal

ApiV1KubernetesAppsDiscoverCreatePodsStatusHashErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_APPS_DISCOVER_CREATE_PODS_STATUS_HASH_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsDiscoverCreatePodsStatusHashErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_apps_discover_create_pods_status_hash_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsDiscoverCreatePodsStatusHashErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_DISCOVER_CREATE_PODS_STATUS_HASH_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_DISCOVER_CREATE_PODS_STATUS_HASH_ERROR_COMPONENT_CODE_VALUES!r}"
    )
