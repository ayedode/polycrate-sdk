from typing import Literal

ApiV1KubernetesAppsUpdateHaEnabledErrorComponentAttr = Literal["ha_enabled"]

API_V1_KUBERNETES_APPS_UPDATE_HA_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsUpdateHaEnabledErrorComponentAttr
] = {
    "ha_enabled",
}


def check_api_v1_kubernetes_apps_update_ha_enabled_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUpdateHaEnabledErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UPDATE_HA_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UPDATE_HA_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
