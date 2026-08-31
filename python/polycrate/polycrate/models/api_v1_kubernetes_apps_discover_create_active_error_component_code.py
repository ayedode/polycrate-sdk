from typing import Literal

ApiV1KubernetesAppsDiscoverCreateActiveErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_APPS_DISCOVER_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsDiscoverCreateActiveErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_apps_discover_create_active_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsDiscoverCreateActiveErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_DISCOVER_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_DISCOVER_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
