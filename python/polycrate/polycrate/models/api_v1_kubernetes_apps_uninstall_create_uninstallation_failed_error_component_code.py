from typing import Literal

ApiV1KubernetesAppsUninstallCreateUninstallationFailedErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_UNINSTALLATION_FAILED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsUninstallCreateUninstallationFailedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_apps_uninstall_create_uninstallation_failed_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsUninstallCreateUninstallationFailedErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_UNINSTALLATION_FAILED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_UNINSTALLATION_FAILED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
