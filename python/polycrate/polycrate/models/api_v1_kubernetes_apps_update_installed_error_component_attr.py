from typing import Literal

ApiV1KubernetesAppsUpdateInstalledErrorComponentAttr = Literal["installed"]

API_V1_KUBERNETES_APPS_UPDATE_INSTALLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsUpdateInstalledErrorComponentAttr
] = {
    "installed",
}


def check_api_v1_kubernetes_apps_update_installed_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUpdateInstalledErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UPDATE_INSTALLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UPDATE_INSTALLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
