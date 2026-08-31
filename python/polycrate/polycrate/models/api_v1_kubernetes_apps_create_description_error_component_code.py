from typing import Literal

ApiV1KubernetesAppsCreateDescriptionErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_APPS_CREATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsCreateDescriptionErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_apps_create_description_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsCreateDescriptionErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_CREATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_CREATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
