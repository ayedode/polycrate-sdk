from typing import Literal

ApiV1KubernetesAppsInstallCreateUninstallationFailedErrorComponentAttr = Literal["uninstallation_failed"]

API_V1_KUBERNETES_APPS_INSTALL_CREATE_UNINSTALLATION_FAILED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsInstallCreateUninstallationFailedErrorComponentAttr
] = {
    "uninstallation_failed",
}


def check_api_v1_kubernetes_apps_install_create_uninstallation_failed_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsInstallCreateUninstallationFailedErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_INSTALL_CREATE_UNINSTALLATION_FAILED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_INSTALL_CREATE_UNINSTALLATION_FAILED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
