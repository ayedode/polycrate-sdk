from typing import Literal

ApiV1KubernetesAppsUninstallCreateInstalledVersionErrorComponentAttr = Literal["installed_version"]

API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_INSTALLED_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsUninstallCreateInstalledVersionErrorComponentAttr
] = {
    "installed_version",
}


def check_api_v1_kubernetes_apps_uninstall_create_installed_version_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUninstallCreateInstalledVersionErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_INSTALLED_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_INSTALLED_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
