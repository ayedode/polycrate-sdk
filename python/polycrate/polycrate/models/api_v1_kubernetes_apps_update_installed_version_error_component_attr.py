from typing import Literal

ApiV1KubernetesAppsUpdateInstalledVersionErrorComponentAttr = Literal["installed_version"]

API_V1_KUBERNETES_APPS_UPDATE_INSTALLED_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsUpdateInstalledVersionErrorComponentAttr
] = {
    "installed_version",
}


def check_api_v1_kubernetes_apps_update_installed_version_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUpdateInstalledVersionErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UPDATE_INSTALLED_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UPDATE_INSTALLED_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
