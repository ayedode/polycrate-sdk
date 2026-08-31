from typing import Literal

ApiV1KubernetesAppsDiscoverCreateInstalledErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_APPS_DISCOVER_CREATE_INSTALLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsDiscoverCreateInstalledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_apps_discover_create_installed_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsDiscoverCreateInstalledErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_DISCOVER_CREATE_INSTALLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_DISCOVER_CREATE_INSTALLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
