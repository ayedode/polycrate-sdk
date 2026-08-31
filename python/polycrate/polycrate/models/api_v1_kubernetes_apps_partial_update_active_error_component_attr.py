from typing import Literal

ApiV1KubernetesAppsPartialUpdateActiveErrorComponentAttr = Literal["active"]

API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsPartialUpdateActiveErrorComponentAttr
] = {
    "active",
}


def check_api_v1_kubernetes_apps_partial_update_active_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsPartialUpdateActiveErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
