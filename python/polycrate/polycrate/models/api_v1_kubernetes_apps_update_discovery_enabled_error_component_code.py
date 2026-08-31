from typing import Literal

ApiV1KubernetesAppsUpdateDiscoveryEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_APPS_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsUpdateDiscoveryEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_apps_update_discovery_enabled_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsUpdateDiscoveryEnabledErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
