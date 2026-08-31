from typing import Literal

ApiV1KubernetesAppsInstallCreateInstalledErrorComponentAttr = Literal["installed"]

API_V1_KUBERNETES_APPS_INSTALL_CREATE_INSTALLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsInstallCreateInstalledErrorComponentAttr
] = {
    "installed",
}


def check_api_v1_kubernetes_apps_install_create_installed_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsInstallCreateInstalledErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_INSTALL_CREATE_INSTALLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_INSTALL_CREATE_INSTALLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
