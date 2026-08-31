from typing import Literal

ApiV1KubernetesAppsUpdateUninstalledErrorComponentAttr = Literal["uninstalled"]

API_V1_KUBERNETES_APPS_UPDATE_UNINSTALLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsUpdateUninstalledErrorComponentAttr
] = {
    "uninstalled",
}


def check_api_v1_kubernetes_apps_update_uninstalled_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUpdateUninstalledErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UPDATE_UNINSTALLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UPDATE_UNINSTALLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
