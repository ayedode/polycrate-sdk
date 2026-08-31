from typing import Literal

ApiV1KubernetesAppsInstallCreateUninstalledErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_APPS_INSTALL_CREATE_UNINSTALLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsInstallCreateUninstalledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_apps_install_create_uninstalled_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsInstallCreateUninstalledErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_INSTALL_CREATE_UNINSTALLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_INSTALL_CREATE_UNINSTALLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
