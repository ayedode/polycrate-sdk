from typing import Literal

ApiV1KubernetesAppsDiscoverCreateByoaErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_APPS_DISCOVER_CREATE_BYOA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsDiscoverCreateByoaErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_apps_discover_create_byoa_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsDiscoverCreateByoaErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_DISCOVER_CREATE_BYOA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_DISCOVER_CREATE_BYOA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
