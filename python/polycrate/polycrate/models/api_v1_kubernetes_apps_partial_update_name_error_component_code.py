from typing import Literal

ApiV1KubernetesAppsPartialUpdateNameErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsPartialUpdateNameErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_apps_partial_update_name_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsPartialUpdateNameErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
