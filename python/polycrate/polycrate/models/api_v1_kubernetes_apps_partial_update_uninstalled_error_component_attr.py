from typing import Literal

ApiV1KubernetesAppsPartialUpdateUninstalledErrorComponentAttr = Literal["uninstalled"]

API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_UNINSTALLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsPartialUpdateUninstalledErrorComponentAttr
] = {
    "uninstalled",
}


def check_api_v1_kubernetes_apps_partial_update_uninstalled_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsPartialUpdateUninstalledErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_UNINSTALLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_UNINSTALLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
