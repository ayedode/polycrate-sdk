from typing import Literal

ApiV1KubernetesAppsDiscoverCreateSourceErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_APPS_DISCOVER_CREATE_SOURCE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsDiscoverCreateSourceErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_apps_discover_create_source_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsDiscoverCreateSourceErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_DISCOVER_CREATE_SOURCE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_DISCOVER_CREATE_SOURCE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
