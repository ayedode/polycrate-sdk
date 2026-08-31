from typing import Literal

ApiV1KubernetesAppsUpdateActiveErrorComponentAttr = Literal["active"]

API_V1_KUBERNETES_APPS_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsUpdateActiveErrorComponentAttr
] = {
    "active",
}


def check_api_v1_kubernetes_apps_update_active_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUpdateActiveErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
