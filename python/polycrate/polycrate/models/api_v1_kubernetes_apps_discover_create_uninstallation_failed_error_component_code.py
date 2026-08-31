from typing import Literal

ApiV1KubernetesAppsDiscoverCreateUninstallationFailedErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_APPS_DISCOVER_CREATE_UNINSTALLATION_FAILED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsDiscoverCreateUninstallationFailedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_apps_discover_create_uninstallation_failed_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsDiscoverCreateUninstallationFailedErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_DISCOVER_CREATE_UNINSTALLATION_FAILED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_DISCOVER_CREATE_UNINSTALLATION_FAILED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
