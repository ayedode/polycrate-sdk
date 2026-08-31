from typing import Literal

ApiV1KubernetesAppsDiscoverCreateInstallationFailedErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_APPS_DISCOVER_CREATE_INSTALLATION_FAILED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsDiscoverCreateInstallationFailedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_apps_discover_create_installation_failed_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsDiscoverCreateInstallationFailedErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_DISCOVER_CREATE_INSTALLATION_FAILED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_DISCOVER_CREATE_INSTALLATION_FAILED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
