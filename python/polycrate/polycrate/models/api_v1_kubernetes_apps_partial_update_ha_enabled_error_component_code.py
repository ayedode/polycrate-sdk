from typing import Literal

ApiV1KubernetesAppsPartialUpdateHaEnabledErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_HA_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsPartialUpdateHaEnabledErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_apps_partial_update_ha_enabled_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsPartialUpdateHaEnabledErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_HA_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_HA_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
