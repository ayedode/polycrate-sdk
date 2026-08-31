from typing import Literal

ApiV1KubernetesAppsUninstallCreateInstalledErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_INSTALLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsUninstallCreateInstalledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_apps_uninstall_create_installed_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsUninstallCreateInstalledErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_INSTALLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_INSTALLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
