from typing import Literal

ApiV1KubernetesAppsPartialUpdateInstalledErrorComponentAttr = Literal["installed"]

API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_INSTALLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsPartialUpdateInstalledErrorComponentAttr
] = {
    "installed",
}


def check_api_v1_kubernetes_apps_partial_update_installed_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsPartialUpdateInstalledErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_INSTALLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_INSTALLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
