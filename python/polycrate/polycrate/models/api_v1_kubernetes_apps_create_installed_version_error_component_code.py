from typing import Literal

ApiV1KubernetesAppsCreateInstalledVersionErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_APPS_CREATE_INSTALLED_VERSION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsCreateInstalledVersionErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_apps_create_installed_version_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsCreateInstalledVersionErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_CREATE_INSTALLED_VERSION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_CREATE_INSTALLED_VERSION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
