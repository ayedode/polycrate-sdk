from typing import Literal

ApiV1KubernetesAppsPartialUpdateSourceErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_SOURCE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsPartialUpdateSourceErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_apps_partial_update_source_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsPartialUpdateSourceErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_SOURCE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_SOURCE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
